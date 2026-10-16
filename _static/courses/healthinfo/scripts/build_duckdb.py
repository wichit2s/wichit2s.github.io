#!/usr/bin/env python3
"""Build a DuckDB healthinfo database from the shared schema + seed.

Uses the same ../sql/ files as the SQLite and PostgreSQL paths, so all
three engines hold identical rows.

Run:
  uv run --with duckdb python scripts/build_duckdb.py
  uv run --with duckdb python scripts/build_duckdb.py -o healthinfo.duckdb
"""
from __future__ import annotations

import argparse
import pathlib
import re

import duckdb

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
SQL = DATA / "sql"


def _strip(text: str, pattern: str) -> str:
    # Drop whole statements matching pattern instead of regex .*?; which
    # truncates at the first semicolon (breaks if a literal ever contains ';').
    stmts = [s for s in text.split(";") if not re.search(pattern, s)]
    return ";".join(stmts)


def _exec_script(con, sql: str) -> None:
    # Execute one statement at a time: DuckDB's execute() multi-statement
    # support varies by version, so don't rely on con.execute(whole_file).
    # Strip full-line -- comments first (seed header contains ';' inside
    # a comment which would otherwise split into a bogus fragment).
    no_comments = "\n".join(
        ln for ln in sql.splitlines() if not ln.strip().startswith("--")
    )
    for stmt in no_comments.split(";"):
        stmt = stmt.strip()
        if stmt:
            con.execute(stmt)


def build(out: pathlib.Path, exclude_diagnoses: bool = False) -> None:
    schema = (SQL / "healthinfo_schema_duckdb.sql").read_text(encoding="utf-8")
    seed = (SQL / "healthinfo_seed.sql").read_text(encoding="utf-8")
    if exclude_diagnoses:
        schema = _strip(schema, r"CREATE TABLE diagnoses\(")
        seed = _strip(seed, r"INSERT INTO diagnoses \(")
    if out.exists():
        out.unlink()
    con = duckdb.connect(str(out))
    _exec_script(con, schema)
    _exec_script(con, seed)
    tables = [r[0] for r in con.execute("SHOW TABLES").fetchall()]
    con.close()
    print(f"built {out} ({', '.join(sorted(tables))})")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "-o", "--out", default=str(DATA / "healthinfo.duckdb"), help="output path"
    )
    ap.add_argument(
        "--exclude-diagnoses",
        action="store_true",
        help="omit the week-8 diagnoses table (pre-08 state)",
    )
    args = ap.parse_args()
    build(pathlib.Path(args.out), args.exclude_diagnoses)


if __name__ == "__main__":
    main()
