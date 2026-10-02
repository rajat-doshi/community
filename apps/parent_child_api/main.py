from fastapi import FastAPI
from apps.parent_child_api.router import router as parent_child_router

app = FastAPI(title="parent-child-api", version="0.1.0")
app.include_router(parent_child_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8005)
