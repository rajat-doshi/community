from fastapi import FastAPI
from apps.split_family_api.router import router as split_family_router

app = FastAPI(title="split-family-api", version="0.1.0")
app.include_router(split_family_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8006)
