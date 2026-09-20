start-api:
	uv run uvicorn apps.family_api.main:app --reload --port 8002

db-setup:
	uv run python packages/database/src/my_database/main.py