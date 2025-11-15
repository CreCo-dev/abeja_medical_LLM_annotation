"""
FastAPI のルーター定義から自動で API 定義書 (Markdown) を生成するスクリプト。
- Request Parameters（Path / Query）
- Request Body（Pydanticモデル）
- Response Model（単体 / List[T]）
- response_model=list[T] を 100% 判定（response_model を直接解析）
- Pydantic v2 / FastAPI v0.110 対応
"""

from pathlib import Path
from typing import get_type_hints, get_origin, get_args, Union, List, Sequence
from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter
from pydantic import BaseModel
from app.main import app


# =========================================================
# 型表記整形ユーティリティ
# =========================================================
def format_type(tp) -> str:
    if tp is None:
        return ""

    origin = get_origin(tp)
    args = get_args(tp)

    # Optional[T] → T
    if origin is Union and len(args) == 2 and type(None) in args:
        inner = [a for a in args if a is not type(None)][0]
        return format_type(inner)

    # list[T] → T[]
    if origin in (list, List, Sequence) and args:
        return f"{format_type(args[0])}[]"

    # datetime.date 等
    if hasattr(tp, "__name__"):
        return tp.__name__

    # <class 'int'> → int
    text = str(tp)
    if text.startswith("<class '") and text.endswith("'>"):
        return text[len("<class '") : -len("'>")]

    # typing.Optional[X] → X
    if text.startswith("typing.Optional["):
        return text.replace("typing.Optional[", "").replace("]", "")

    # typing.X → X
    if text.startswith("typing."):
        return text.replace("typing.", "")

    return text


# =========================================================
# 型安全 issubclass
# =========================================================
def issubclass_safe(obj, cls):
    try:
        return isinstance(obj, type) and issubclass(obj, cls)
    except Exception:
        return False


# =========================================================
# 全ルート収集（include_router対応）
# =========================================================
def collect_all_routes(router_or_app) -> list[APIRoute]:
    routes: list[APIRoute] = []
    for r in getattr(router_or_app, "routes", []):
        if isinstance(r, APIRoute):
            routes.append(r)
        elif isinstance(r, APIRouter) or hasattr(r, "routes"):
            routes.extend(collect_all_routes(r))
    return routes


# =========================================================
# Request Body モデル抽出
# =========================================================
def extract_models_from_body(route: APIRoute):
    models = set()

    for param in route.dependant.body_params:
        typ = getattr(param, "annotation", None)

        if typ is None and hasattr(param, "field"):
            typ = getattr(param.field, "outer_type_", None)

        if typ is None:
            continue

        origin = get_origin(typ)
        args = get_args(typ)

        if origin in (list, List, Sequence) and args:
            typ = args[0]

        if issubclass_safe(typ, BaseModel):
            models.add(typ)

    return list(models)


# =========================================================
# Response Model 抽出（response_model 直接解析 → 最も安定）
# =========================================================
def extract_models_from_response(route: APIRoute):
    """
    FastAPI response_model を直接解析して List[T] を安全に判定する。
    戻り値: (is_list: bool, models: set[type[BaseModel]])
    """
    model = route.response_model

    if model is None or isinstance(model, bool):
        return False, set()

    origin = get_origin(model)
    args = get_args(model)

    # ====== list[T] / List[T] / Sequence[T] ======
    if origin in (list, List, Sequence) and args:
        inner = args[0]
        if issubclass_safe(inner, BaseModel):
            return True, {inner}
        return True, set()

    # ====== 単体 BaseModel ======
    if issubclass_safe(model, BaseModel):
        return False, {model}

    return False, set()


# =========================================================
# Path / Query Parameter 抽出
# =========================================================
def extract_query_and_path_params(route: APIRoute):
    params = []
    all_params = route.dependant.path_params + route.dependant.query_params

    for param in all_params:
        annotation = getattr(param, "annotation", None)
        if annotation is None and hasattr(param, "field"):
            annotation = getattr(param.field, "annotation", None)

        name = getattr(param, "name", None) or getattr(param, "param_name", "")
        required = "Y" if getattr(param, "required", False) else ""
        desc = getattr(param, "description", "") or ""

        params.append((name, format_type(annotation), required, desc))

    return params


# =========================================================
# Pydantic BaseModel → Markdown
# =========================================================
def model_to_markdown(model: type[BaseModel], title: str):
    lines = [
        f"#### {title}",
        "",
        "| フィールド | 型 | 必須 | 説明 |",
        "|---|---|:--:|---|",
    ]

    type_hints = get_type_hints(model)

    for name, field in model.model_fields.items():
        field_type = type_hints.get(name, field.annotation)
        lines.append(
            f"| `{name}` | {format_type(field_type)} | "
            f"{'Y' if field.is_required() else ''} | {field.description or ''} |"
        )

    lines.append("")
    return "\n".join(lines)


# =========================================================
# Markdown 出力
# =========================================================
def export_api_docs(app: FastAPI, output_path: str = "docs/api_schema.md"):
    routes = collect_all_routes(app)
    output = ["# API 定義書", f"総ルート数: {len(routes)}", ""]

    for route in routes:
        path = route.path
        methods = ", ".join(sorted(route.methods - {"HEAD", "OPTIONS"}))
        summary = getattr(route, "summary", "")
        description = getattr(route, "description", "")

        output += [f"## {methods} {path}", ""]

        if summary:
            output.append(f"**概要:** {summary}")
        if description:
            output.append(f"**説明:** {description}")
        output.append("")

        # ---------------------
        # Request Parameters
        # ---------------------
        params = extract_query_and_path_params(route)
        if params:
            output += [
                "### Request Parameters",
                "",
                "| パラメータ | 型 | 必須 | 説明 |",
                "|---|---|:--:|---|",
            ]
            for name, typ, required, desc in params:
                output.append(f"| `{name}` | {typ} | {required} | {desc} |")
            output.append("")

        # ---------------------
        # Request Body
        # ---------------------
        body_models = extract_models_from_body(route)
        if body_models:
            for model in body_models:
                output += [model_to_markdown(model, f"Request Body ({model.__name__})")]

        # ---------------------
        # Response
        # ---------------------
        is_list, models = extract_models_from_response(route)

        if is_list and models:
            model_name = list(models)[0].__name__
            output.append(f"**レスポンス形式:** List[{model_name}]\n")
        elif is_list:
            output.append("**レスポンス形式:** List[Any]\n")
        elif models:
            model_name = list(models)[0].__name__
            output.append(f"**レスポンス形式:** {model_name}\n")
        else:
            output.append("**レスポンス形式:** （未指定）\n")

        for model in models:
            output.append(model_to_markdown(model, f"Response Model ({model.__name__})"))

        output.append("---")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(output), encoding="utf-8")
    print(f"[EXPORT] {output_path} generated. Total routes: {len(routes)}")


# =========================================================
# 実行
# =========================================================
if __name__ == "__main__":
    export_api_docs(app)
