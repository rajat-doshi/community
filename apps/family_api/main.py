from fastapi import FastAPI
from apps.family_api.router import router as family_router

app = FastAPI(
    title="Family API",
    description="Documentation for the Family management service.",
    version="1.0.0",
)

app.include_router(family_router)


@app.get("/")
def read_root():
    return {"message": "Hello from family-api!"}


@app.on_event("startup")
async def startup_event():
    print("Family API is starting up...")
