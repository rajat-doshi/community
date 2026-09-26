from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from my_database.db import get_db

from apps.users_api.model import fetch_users_list_model

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/fetch-users-list")
async def fetch_users_list(db: Session = Depends(get_db)):
    return fetch_users_list_model(db)
