from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from my_database.model.users.main import User
from apps.users_api.users.type import Type_UserList, Type_User
from apps.users_api.utils.utils import (
    TYPE_SUCCESS_RESPONSE,
    TYPE_ERROR_RESPONSE,
    SUCCESS_RESPONSE,
    ERROR_RESPONSE,
)
from typing import List


def model_fetch_users_list(
    db: Session,
) -> TYPE_SUCCESS_RESPONSE[List[Type_User]] | TYPE_ERROR_RESPONSE[str]:
    try:
        users = db.query(User).all()
        users_list = Type_UserList.validate_python(users)
        return SUCCESS_RESPONSE(data=users_list, msg="Users fetched successfully", status_code=200)
    except Exception as e:
        print(f"Error fetching users: {e}")
        return ERROR_RESPONSE(msg="Error fetching users", status_code=500, data=str(e))


def model_create_user_list(
    db: Session, user_data: Type_User
) -> TYPE_SUCCESS_RESPONSE[Type_User] | TYPE_ERROR_RESPONSE[str]:
    try:
        print(f"Creating user with data: {user_data}")
        new_user = User(**user_data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return SUCCESS_RESPONSE(data=new_user, msg="User created successfully", status_code=201)
    except IntegrityError as e:
        db.rollback()
        return ERROR_RESPONSE(msg="Error creating user", status_code=400, data=str(e.orig))
    except Exception as e:
        print(f"Error creating user: {e}")
        return ERROR_RESPONSE(msg="Error creating user", status_code=500, data=str(e))
