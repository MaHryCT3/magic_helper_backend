#!/bin/sh

echo "Make migration"
alembic upgrade head

echo "Statring aplication..."
uvicorn app:app --port 443


