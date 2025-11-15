"""
FastAPI のルーター定義から API 定義書 (Markdown) を自動生成するスクリプト。

■対応機能
- タグ（router.tags）ごとに章分け
- パスパラメータ / クエリパラメータ
- リクエストボディ（Pydanticモデル）
- レスポンス形式（単体 / List[T]）
- レスポンスモデル（Pydanticモデル）
- 型表記の簡潔化（int, str, date, time, Model[]）
- response_model=list[T] を正しく検知
- FastAPI v0.110 / Pydantic v2 対応
"""

from pathlib import Path
from typing import get_type_hints, get_origin, get_args, Union, List, Sequence
from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter
from pydantic import BaseModel
from app.main import app


# =========================================================
# 型表記整形
# =========================================================
def format_type(tp) -> str:
    if tp is None:
        return ""

    # Optional[T]
    origin = get_origin(tp)
    args = get_args(tp)
    if origin is Union and len(args) == 2 and type(None) in args:
        inner = [x for x in args if x is not type(None)][0]
        return format_type(inner)

    # list[T]
    if origin in (list, List, Sequence) and args:
        return f"{format_type(args[0])}[]"

    # datetime.date など
    if hasattr(tp, "__name__"):
        return tp.__name__

    text = str(tp)

    # <class 'int'> → int
    if text.startswith("<class '") and text.endswith("'>"):
        return text[8:-2]

    if text.startswith("typing."):
        return text.replace("typing.", "")

    return text


# =========================================================
# issubclass 安全版
# =========================================================
def issubclass_safe(obj, cls):
    try:
        return isinstance(obj, type) and issubclass(obj, cls)
    except Exception:
        return False


# =========================================================
# include_router 配下も含めて全ルート収集
# =========================================================
def collect_all_routes(router_or_app) -> list[APIRoute]:
    routes: list[APIRoute] = []
    for r in getattr(router_or_app, "routes", []):
        if isinstance(r, APIRoute):
            routes.append(r)
        elif isinstance(r, APIRouter):
            routes.extend(collect_all_routes(r))
    return routes


# =========================================================
# Request Body 抽出（Pydanticモデル）
# =========================================================
def extract_models_from_body(route: APIRoute):
    models = set()

    for param in route.dependant.body_params:

        # FastAPI v0.110 + Pydantic v2 では field_info.annotation が正しい
        typ = getattr(param.field_info, "annotation", None)

        # Fallbacks
        if typ is None:
            typ = getattr(param, "annotation", None)
        if typ is None and hasattr(param, "field"):
            typ = getattr(param.field, "outer_type_", None)
        if typ is None:
            continue

        # Optional[T]
        origin = get_origin(typ)
        args = get_args(typ)
        if origin is Union and args:
            non_none = [a for a in args if a is not type(None)]
            if non_none:
                typ = non_none[0]
                origin = get_origin(typ)
                args = get_args(typ)

        # List[T]
        if origin in (list, List, Sequence) and args:
            typ = args[0]

        if issubclass_safe(typ, BaseModel):
            models.add(typ)

    return list(models)


# =========================================================
# Response Model 抽出（response_model を直接解析）
# =========================================================
def extract_models_from_response(route: APIRoute):
    model = route.response_model

    #print(f"[DEBUG] response_model for {route.path} = {model!r}")

    if model is None or isinstance(model, bool):
        return False, set()

    origin = get_origin(model)
    args = get_args(model)

    # list[T] / List[T]
    if origin in (list, List, Sequence) and args:
        inner = args[0]
        if issubclass_safe(inner, BaseModel):
            return True, {inner}
        return True, set()

    # 単体モデル
    if issubclass_safe(model, BaseModel):
        return False, {model}

    return False, set()


# =========================================================
# パス / クエリ パラメータ抽出
# =========================================================
def extract_path_and_query_params(route: APIRoute):
    path_list = []
    query_list = []

    # Path params
    for param in route.dependant.path_params:
        ann = getattr(param, "annotation", None) or getattr(getattr(param, "field", None), "annotation", None)
        path_list.append((param.name, format_type(ann), "Y", ""))

    # Query params
    for param in route.dependant.query_params:
        ann = getattr(param, "annotation", None) or getattr(getattr(param, "field", None), "annotation", None)
        req = "Y" if param.required else ""
        query_list.append((param.name, format_type(ann), req, ""))

    return path_list, query_list


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
# Markdown 出力（タグごとに章分け）
# =========================================================
def export_api_docs(app: FastAPI, output_path: str = "docs/api_schema.md"):
    routes = collect_all_routes(app)

    # タグ → ルート一覧
    tag_map: dict[str, list[APIRoute]] = {}
    for r in routes:
        tags = r.tags or ["default"]
        for t in tags:
            tag_map.setdefault(t, []).append(r)

    output = ["# API 定義書", ""]

    # ======== タグごとに出力 ========
    for tag, tag_routes in tag_map.items():
        output.append(f"# {tag}")
        output.append("")

        for route in tag_routes:

            path = route.path
            methods = ", ".join(sorted(route.methods - {"HEAD", "OPTIONS"}))
            summary = route.summary or ""
            description = route.description or ""

            output += [f"## {methods} {path}", ""]

            if summary:
                output.append(f"**概要:** {summary}\n")
            if description:
                output.append(f"**説明:** {description}\n")

            output.append(f"### リクエスト\n")

            # ----- Path / Query -----
            path_params, query_params = extract_path_and_query_params(route)

            if path_params:
                output += [
                    "#### パスパラメータ",
                    "",
                    "| パラメータ | 型 | 必須 | 説明 |",
                    "|---|---|:--:|---|",
                ]
                for name, typ, req, desc in path_params:
                    output.append(f"| `{name}` | {typ} | {req} | {desc} |")
                output.append("")

            if query_params:
                output += [
                    "#### クエリパラメータ",
                    "",
                    "| パラメータ | 型 | 必須 | 説明 |",
                    "|---|---|:--:|---|",
                ]
                for name, typ, req, desc in query_params:
                    output.append(f"| `{name}` | {typ} | {req} | {desc} |")
                output.append("")

            if (path_params == []) and (query_params == []) :
                output.append("None")

            # ----- Request Body -----
            body_models = extract_models_from_body(route)
            for model in body_models:
                output.append(model_to_markdown(model, f"ボディ ({model.__name__})"))

            # ----- Response -----
            is_list, models = extract_models_from_response(route)

            output.append(f"### レスポンス\n")

            # response_model=None → dict とみなして出力
            if route.response_model is None:
                output.append("**形式:** dict\n")
                output.append("**モデル:**  Any")
                continue

            if is_list and models:
                name = list(models)[0].__name__
                output.append(f"**形式:** List[{name}]\n")
            elif is_list:
                output.append("**形式:** List[Any]\n")
            elif models:
                name = list(models)[0].__name__
                output.append(f"**形式:** {name}\n")
            else:
                None
                #output.append("### レスポンス\n")

            for model in models:
                output.append(model_to_markdown(model, f"**モデル:** {model.__name__}"))

            output.append("---")

    # 書き込み
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(output), encoding="utf-8")

    print(f"[EXPORT] {output_path} generated.")


# =========================================================
# 実行
# =========================================================
if __name__ == "__main__":
    export_api_docs(app)
