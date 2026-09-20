from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from my_database.db import get_db

from apps.family_api.type import Type_Family_List
from apps.users_api.utils.utils import TYPE_SUCCESS_RESPONSE, TYPE_ERROR_RESPONSE
from apps.family_api.model.main import fetch_family_users_list


router = APIRouter(prefix="/family", tags=["Family"])


@router.get(
    "/fetch-users-list",
    response_model=TYPE_SUCCESS_RESPONSE[Type_Family_List] | TYPE_ERROR_RESPONSE[str],
)
def fetch_users_list(db: Session = Depends(get_db)):
    return fetch_family_users_list(db)
