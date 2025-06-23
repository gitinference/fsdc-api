#!/bin/bash
set -e

echo "Running Alembic migrations..."
alembic upgrade head

echo "Seeding initial data (if needed)..."
python -c "from src.core.db import _seed_initial_data, get_session; _seed_initial_data(next(get_session()))"

echo "Starting FastAPI app..."
exec "$@"
