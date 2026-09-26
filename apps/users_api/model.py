from sqlalchemy.orm import Session

from community.db.model.user_model import User


def fetch_users_list_model(db: Session):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        print(f"Error fetching users list: {e}")
        return {"error": "Failed to fetch users list"}
