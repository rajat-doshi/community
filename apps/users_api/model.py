from sqlalchemy.orm import Session
from my_database.model.users.main import User
from shared_core.utility.api_response import SUCCESS_RESPONSE, ERROR_RESPONSE


def fetch_users_list_model(db: Session):
    try:
        users = db.query(User).all()
        return SUCCESS_RESPONSE(data=users, msg="Users fetched successfully", status_code=200)
    except Exception as e:
        print(f"Error fetching users list: {e}")
        return ERROR_RESPONSE(data=None, msg="Failed to fetch users list", status_code=500)
