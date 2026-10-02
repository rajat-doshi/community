from fastapi import APIRouter, Depends
from my_database.db import get_db
from sqlalchemy.orm import Session
from apps.family_api.model import create_family_model, fetch_family_list_model

router = APIRouter(
    prefix="/family",
    tags=["family"],
)


@router.get("/fetch-family-list")
async def fetch_family_list(db: Session = Depends(get_db)):
    return fetch_family_list_model(db)


@router.post("/create-family")
async def create_family(family_data: dict, db: Session = Depends(get_db)):
    return create_family_model(db, family_data)
