from fastapi import FastAPI
from apps.users_api.users.router import user_router

app = FastAPI()
app.include_router(user_router)


