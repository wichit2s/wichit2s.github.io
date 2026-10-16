#!/usr/bin/env python3
"""Build a SQLite healthinfo database from the shared schema + seed.

The schema and seed live in ../sql/ and are engine-portable, so the same
files drive the DuckDB builder and the PostgreSQL setup script.

Examples
--------
python scripts/build_sqlite.py                       # -> healthinfo.db (full)
python scripts/build_sqlite.py --exclude-diagnoses   # week-5/6/7 snapshot
python scripts/build_sqlite.py -o healthinfo-pre-08.db --exclude-diagnoses
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sqlite3

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
SQL = DATA / "sql"


def _strip(text: str, pattern: str) -> str:
    # Drop whole statements matching pattern instead of regex .*?; which
    # truncates at the first semicolon (breaks if a literal ever contains ';').
    stmts = [s for s in text.split(";") if not re.search(pattern, s)]
    return ";".join(stmts)


def build(out: pathlib.Path, exclude_diagnoses: bool = False) -> None:
    schema = (SQL / "healthinfo_schema_sqlite.sql").read_text(encoding="utf-8")
    seed = (SQL / "healthinfo_seed.sql").read_text(encoding="utf-8")
    if exclude_diagnoses:
        schema = _strip(schema, r"CREATE TABLE diagnoses\(")
        seed = _strip(seed, r"INSERT INTO diagnoses \(")
    if out.exists():
        out.unlink()
    con = sqlite3.connect(out)
    con.executescript(schema)
    con.executescript(seed)
    con.commit()
    n = con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    con.close()
    print(f"built {out} ({', '.join(t[0] for t in n)})")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "-o", "--out", default=str(DATA / "healthinfo.db"), help="output .db path"
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
