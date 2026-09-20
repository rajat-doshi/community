from fastapi import FastAPI
from apps.users_api.users.router import user_router
# from shared_core.db.database import Base, engine

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    print("Users API is starting up...")
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)