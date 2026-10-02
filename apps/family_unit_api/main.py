from fastapi import FastAPI
from apps.family_unit_api.router import router as family_unit_router

app = FastAPI(title="family-unit-api", version="0.1.0")
app.include_router(family_unit_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8004)
