from fastapi import APIRouter, Depends
from my_database.db import get_db
from sqlalchemy.orm import Session
from apps.split_family_api.model import (
    create_split_family_model,
    delete_split_family_model,
    fetch_split_families_list,
    fetch_split_family_by_id_model,
    update_split_family_model,
)
from apps.split_family_api.type import SplitFamilyType
from shared_core.utility.api_response import TYPE_ERROR_RESPONSE, TYPE_SUCCESS_RESPONSE

router = APIRouter(
    prefix="/split-family",
    tags=["split-family"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/list",
    response_model=TYPE_SUCCESS_RESPONSE[list[SplitFamilyType]] | TYPE_ERROR_RESPONSE[str],
)
async def read_split_families(db: Session = Depends(get_db)):
    return fetch_split_families_list(db)


@router.post(
    "/create",
    response_model=TYPE_SUCCESS_RESPONSE[SplitFamilyType] | TYPE_ERROR_RESPONSE[str],
)
async def create_split_family(split_family: SplitFamilyType, db: Session = Depends(get_db)):
    return create_split_family_model(db, split_family)


@router.post(
    "/update",
    response_model=TYPE_SUCCESS_RESPONSE[SplitFamilyType] | TYPE_ERROR_RESPONSE[str],
)
def update_split_family(split_family: SplitFamilyType, db: Session = Depends(get_db)):
    return update_split_family_model(db, split_family)


@router.get("/health")
async def health_check():
    return {"status": "Split-family API is healthy"}


@router.get(
    "/{id}",
    response_model=TYPE_SUCCESS_RESPONSE[SplitFamilyType] | TYPE_ERROR_RESPONSE[str],
)
async def read_split_family(id: int, db: Session = Depends(get_db)):
    return fetch_split_family_by_id_model(db, id)


@router.delete(
    "/{id}",
    response_model=TYPE_SUCCESS_RESPONSE[SplitFamilyType] | TYPE_ERROR_RESPONSE[str],
)
def delete_split_family(id: int, db: Session = Depends(get_db)):
    return delete_split_family_model(db, id)
