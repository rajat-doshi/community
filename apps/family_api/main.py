from fastapi import FastAPI
from apps.family_api.router import router as family_router

app = FastAPI()
app.include_router(family_router)


@app.on_event("startup")
async def startup_event():
    print("Family API is starting up...")
