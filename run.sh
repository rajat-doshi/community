#!/bin/bash

# Ensure both servers stop when you press Ctrl+C
trap "kill 0" EXIT

echo "Starting Users API on port 8000..."
uv run uvicorn apps.users_api.main:app --reload --port 8000 &

echo "Starting Family API on port 8001..."
uv run uvicorn apps.family_api.main:app --reload --port 8001 &

# Wait for all background processes to finish
wait