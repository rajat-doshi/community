from my_database.model.family.main import Family
from shared_core.utility.api_response import SUCCESS_RESPONSE, ERROR_RESPONSE


def fetch_family_list_model(db):
    try:
        families = db.query(Family).all()
        return SUCCESS_RESPONSE(
            data=families, msg="Family list fetched successfully.", status_code=200
        )
    except Exception as e:
        return ERROR_RESPONSE(data=None, msg=str(e), status_code=500)


def create_family_model(db, family_data):
    try:
        new_family = Family(**family_data.dict())
        db.add(new_family)
        db.commit()
        db.refresh(new_family)
        return SUCCESS_RESPONSE(
            data=new_family, msg="Family created successfully.", status_code=201
        )
    except Exception as e:
        db.rollback()
        return ERROR_RESPONSE(data=None, msg=str(e), status_code=500)
