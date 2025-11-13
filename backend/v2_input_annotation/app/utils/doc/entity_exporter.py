"""
エンティティ定義からMarkdown形式のテーブル定義書を出力するスクリプト（和名＋特性自動判定）

実行方法:
docker compose exec backend_v2_input_annotation python -m app.utils.doc.entity_exporter
※./app/docs/entity.mdに作成される
"""

from pathlib import Path
from sqlalchemy import UniqueConstraint
from app.db.database import Base
# 全エンティティをimportしてmetadataに登録
from app.db.entities import karte, discharge_summary, stroke_patient, user_account


def get_table_unique_constraints(table):
    """テーブル内のUnique制約一覧を抽出（複合・単一の両方）"""
    unique_constraints = []
    for constraint in table.constraints:
        if isinstance(constraint, UniqueConstraint):
            cols = list(constraint.columns.keys())
            unique_constraints.append(cols)
    return unique_constraints


def describe_column(col, table_uniques):
    """カラムの特性を自動で説明文として返す（NOT NULL除外）"""
    desc_parts = []

    # 主キー
    if col.primary_key:
        desc_parts.append("主キー")

    # 外部キー
    if col.foreign_keys:
        for fk in col.foreign_keys:
            target = f"{fk.column.table.name}.{fk.column.name}"
            desc_parts.append(f"外部キー({target})")

    # 単一カラムの一意制約（複数列UKはテーブルで扱う）
    for uq_cols in table_uniques:
        if len(uq_cols) == 1 and col.name == uq_cols[0]:
            desc_parts.append("一意制約")

    # デフォルト値
    if col.default is not None:
        desc_parts.append(f"デフォルト={col.default.arg}")

    return "、".join(desc_parts) if desc_parts else ""


def describe_table_uniques(table_uniques):
    """複合Unique制約をMarkdown形式で整形"""
    lines = []
    multi_uqs = [uq for uq in table_uniques if len(uq) > 1]
    if not multi_uqs:
        return lines

    lines.append("**一意制約(複合)**")
    for uq in multi_uqs:
        joined = ", ".join([f"`{c}`" for c in uq])
        lines.append(f"- {joined}")
    lines.append("")
    return lines


def describe_relations(table):
    """テーブルに定義されたリレーション(FK)一覧"""
    rel_lines = []
    for fk in table.foreign_keys:
        rel_lines.append(f"- `{fk.parent.name}` → `{fk.column.table.name}`.`{fk.column.name}`")
    return rel_lines


def metadata_to_markdown(metadata):
    lines = []
    for table in metadata.tables.values():
        tinfo = table.info or {}
        rels = describe_relations(table)
        uniques = get_table_unique_constraints(table)

        lines += [f"## {tinfo.get('ja_name', table.name)} (`{table.name}`)", ""]

        # 複合UKの出力
        uniq_lines = describe_table_uniques(uniques)
        if uniq_lines:
            lines += uniq_lines

        # リレーション出力
        if rels:
            lines += ["**リレーション**", *rels, ""]

        # テーブル構造
        lines += [
            "| 物理名 | 型 | Not Null | 和名 | 説明 |",
            "|---|---|:--:|---|---|",
        ]

        for col in table.columns:
            cinfo = col.info or {}
            col_type = str(col.type)
            not_null = "Y" if not col.nullable else ""
            desc = describe_column(col, uniques)
            lines.append(
                f"| `{col.name}` | {col_type} | {not_null} | {cinfo.get('ja_name', '')} | {desc} |"
            )

        lines.append("")  # テーブルごとに空行

    return "\n".join(lines)


def export_entity_markdown(output_path: str = "docs/entity.md"):
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    md = metadata_to_markdown(Base.metadata)
    Path(output_path).write_text(md, encoding="utf-8")
    print(f"[EXPORT] {output_path} generated.")


if __name__ == "__main__":
    export_entity_markdown()
