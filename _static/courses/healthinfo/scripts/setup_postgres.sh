#!/usr/bin/env bash
# Create/load the PostgreSQL "healthinfo" database from the portable SQL.
#
#   ./scripts/setup_postgres.sh [dbname]
#
# Works with a local PostgreSQL 14+ (Homebrew/Debian) or a cloud instance
# reachable via standard PG* env vars (PGHOST, PGUSER, PGPASSWORD, ...).
set -euo pipefail

DB="${1:-healthinfo}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA="$(dirname "$HERE")"
SCHEMA="$DATA/sql/healthinfo_schema_postgres.sql"
SEED="$DATA/sql/healthinfo_seed.sql"

command -v psql >/dev/null 2>&1 || {
  echo "psql not found. Install PostgreSQL 14+ (e.g. 'brew install postgresql@16')." >&2
  exit 1
}

echo "==> ensuring role/database '$DB' exists"
createdb "$DB" 2>/dev/null || echo "    (database already exists, continuing)"

echo "==> loading schema"
psql -v ON_ERROR_STOP=1 -q -d "$DB" -f "$SCHEMA"

echo "==> loading seed (contains intentional orphan prescription 99999 for week-7)"
psql -v ON_ERROR_STOP=1 -q -d "$DB" -f "$SEED"

echo "==> done. Try:  psql -d $DB -c 'SELECT gender, COUNT(*) FROM patients GROUP BY gender;'"
