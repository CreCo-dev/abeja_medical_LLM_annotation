"""
FastAPI のルーター定義から自動的に API 定義書 (Markdown) を生成するスクリプト。
- GET /xxx?param=... のクエリ・パスパラメータ対応
- List[Model] レスポンス対応
- Pydantic v2 環境対応
"""

from pathlib import Path
from typing import get_type_hints, get_origin, get_args
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel
from app.main import app


def issubclass_safe(obj, cls):
    try:
        return isinstance(obj, type) and issubclass(obj, cls)
    except Exception:
        return False


def model_to_markdown(model: type[BaseModel], title: str):
    """PydanticモデルをMarkdown形式に変換"""
    lines = [f"#### {title}", "", "| フィールド | 型 | 必須 | 説明 |", "|---|---|:--:|---|"]
    type_hints = get_type_hints(model)
    for name, field in model.model_fields.items():
        field_type = str(type_hints.get(name, field.annotation))
        required = "Y" if field.is_required() else ""
        desc = field.description or ""
        lines.append(f"| `{name}` | {field_type} | {required} | {desc} |")
    lines.append("")
    return "\n".join(lines)


def extract_models_from_body(route: APIRoute):
    """リクエストボディに含まれるPydanticモデルを抽出（v2対応）"""
    models = set()
    for param in route.dependant.body_params:
        # Pydantic v2 では field がない場合がある
        typ = getattr(param, "annotation", None)
        if typ is None and hasattr(param, "field"):
            typ = getattr(param.field, "outer_type_", None)
        if typ is None:
            continue

        origin = get_origin(typ)
        args = get_args(typ)
        if origin in (list, tuple, set) and args:
            typ = args[0]

        if issubclass_safe(typ, BaseModel):
            models.add(typ)
    return list(models)


def extract_models_from_response(route: APIRoute):
    """レスポンスモデルを抽出（List[Model]対応）"""
    models = set()
    model = route.response_model
    if model:
        origin = get_origin(model)
        args = get_args(model)
        if origin in (list, tuple, set) and args:
            model = args[0]
        if issubclass_safe(model, BaseModel):
            models.add(model)
    return list(models)


def extract_query_and_path_params(route: APIRoute):
    """クエリパラメータとパスパラメータ情報を抽出（v2対応）"""
    params = []
    all_params = route.dependant.path_params + route.dependant.query_params

    for param in all_params:
        # v2: annotation が直接ある
        annotation = getattr(param, "annotation", None)
        if annotation is None and hasattr(param, "field"):
            annotation = getattr(param.field, "annotation", None)

        name = getattr(param, "name", None) or getattr(param, "param_name", "")
        typ = getattr(annotation, "__name__", str(annotation))
        required = "Y" if getattr(param, "required", False) else ""
        desc = getattr(param, "description", "") or ""
        params.append((name, typ, required, desc))

    return params


def export_api_docs(app: FastAPI, output_path: str = "docs/api_schema.md"):
    """FastAPIルーターを解析しMarkdown出力"""
    output = ["# API 定義書", ""]

    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue

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

        # パス・クエリパラメータ
        params = extract_query_and_path_params(route)
        if params:
            output += [
                "#### パス・クエリパラメータ",
                "",
                "| パラメータ | 型 | 必須 | 説明 |",
                "|---|---|:--:|---|",
            ]
            for name, typ, required, desc in params:
                output.append(f"| `{name}` | {typ} | {required} | {desc} |")
            output.append("")

        # リクエストモデル
        for model in extract_models_from_body(route):
            output += [model_to_markdown(model, f"Request Model ({model.__name__})")]

        # レスポンスモデル
        for model in extract_models_from_response(route):
            output += [model_to_markdown(model, f"Response Model ({model.__name__})")]

        output.append("---")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(output), encoding="utf-8")
    print(f"[EXPORT] {output_path} generated.")


if __name__ == "__main__":
    export_api_docs(app)
