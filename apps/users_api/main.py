from fastapi import FastAPI

from apps.users_api.router import router as user_router

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    print("Users API is starting up...")
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
