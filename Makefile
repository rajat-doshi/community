start-family-api:
	uv run uvicorn apps.family_api.main:app --reload --port 8002

start-users-api:
	uv run uvicorn apps.users_api.main:app --reload --port 8001

db-setup:
	uv run python packages/database/src/my_database/main.py