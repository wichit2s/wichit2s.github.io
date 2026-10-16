# healthinfo — three database engines, one dataset

The course teaches the **same SQL** on three engines:

| Engine | File / service | Best for |
|---|---|---|
| **SQLite** | `healthinfo.db` (single file) | zero-setup, embedded, teaching SQL basics |
| **DuckDB** | `healthinfo.duckdb` (single file) | columnar analytics, reads CSV/Parquet |
| **PostgreSQL** | server database `healthinfo` | client/server, roles, `GRANT`, production |

All three are built from the **same portable** files in `../sql/`:

- `healthinfo_seed.sql` — identical rows for every engine
- `healthinfo_schema_sqlite.sql`, `healthinfo_schema_duckdb.sql`, `healthinfo_schema_postgres.sql`

## Build SQLite

```bash
python scripts/build_sqlite.py                    # -> ../healthinfo.db (with diagnoses)
python scripts/build_sqlite.py --exclude-diagnoses -o ../healthinfo-pre-08.db
```

## Build DuckDB

```bash
uv run --with duckdb python scripts/build_duckdb.py   # -> ../healthinfo.duckdb
```

Or connect in Python:

```python
import duckdb
con = duckdb.connect("healthinfo.duckdb")
con.execute("SELECT gender, COUNT(*) FROM patients GROUP BY gender").df()
```

## Set up PostgreSQL (14+)

```bash
# local Homebrew (macOS): start once, then load
brew services start postgresql@16
./scripts/setup_postgres.sh            # creates db 'healthinfo' and loads schema+seed
psql -d healthinfo -c '\dt'
```

For a cloud/managed instance, set `PGHOST PGPORT PGUSER PGPASSWORD` and run the
same script. The Python driver used in the notebooks is `psycopg[binary]`:

```python
import psycopg
with psycopg.connect("dbname=healthinfo user=$USER") as conn:
    print(conn.execute("SELECT COUNT(*) FROM patients").fetchone())
```

## Week-8 snapshots

- `healthinfo-pre-08.db`  — week-7 end state (patients, prescriptions, referrals)
- `healthinfo-post-08.db` — adds the week-8 `diagnoses` table
