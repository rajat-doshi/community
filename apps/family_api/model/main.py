from my_database.model.family.main import Family
from apps.family_api.type import Type_Single_Family
from apps.users_api.utils.utils import SUCCESS_RESPONSE, ERROR_RESPONSE


def fetch_family_users_list(db):
    try:
        families = db.query(Family).all()
        family_list = [Type_Single_Family.model_validate(family) for family in families]
        return SUCCESS_RESPONSE(
            data=family_list, msg="Family users fetched successfully", status_code=200
        )
    except Exception as e:
        print(f"Error fetching family users: {e}")
        return ERROR_RESPONSE(data=str(e), msg="Error fetching family users", status_code=500)
