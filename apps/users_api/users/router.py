from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from apps.users_api.users.model import model_fetch_users_list, model_create_user_list
from shared_core.db.database import get_db
from apps.users_api.users.type import Type_UserList, Type_User
from apps.users_api.utils.utils import TYPE_SUCCESS_RESPONSE, TYPE_ERROR_RESPONSE
user_router = APIRouter(prefix="/users", tags=["Users"])
from shared_core.test import test

@user_router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return model_fetch_users_list(db)



@user_router.get("/fetch-users-list")
def fetch_users_list(db: Session = Depends(get_db)):
    return model_fetch_users_list(db)

@user_router.post("/create-user", response_model=TYPE_SUCCESS_RESPONSE[Type_User]| TYPE_ERROR_RESPONSE[str])
def create_user(userData: Type_User,db: Session = Depends(get_db)):
    return model_create_user_list(db, userData)