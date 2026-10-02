from fastapi import FastAPI
from apps.members_api.routers import router as members_router

app = FastAPI(title="members-api", version="0.1.0")
app.include_router(members_router)


if __name__ == "__main__":
    pass
