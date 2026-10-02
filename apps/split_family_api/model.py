from my_database.model.split_family import SplitFamily
from shared_core.utility.api_response import ERROR_RESPONSE, SUCCESS_RESPONSE


def fetch_split_families_list(db):
    try:
        split_families = db.query(SplitFamily).all()
        return SUCCESS_RESPONSE(split_families, "Split-family records fetched successfully", 200)
    except Exception as e:
        return ERROR_RESPONSE(str(e), "Error fetching split-family records", 500)


def create_split_family_model(db, split_family_data):
    try:
        new_split_family = SplitFamily(**split_family_data.dict())
        db.add(new_split_family)
        db.commit()
        db.refresh(new_split_family)
        return SUCCESS_RESPONSE(new_split_family, "Split-family record created successfully", 201)
    except Exception as e:
        db.rollback()
        return ERROR_RESPONSE(str(e), "Error creating split-family record", 500)


def update_split_family_model(db, split_family_data):
    try:
        split_family = db.query(SplitFamily).filter(SplitFamily.id == split_family_data.id).first()
        if not split_family:
            return ERROR_RESPONSE("Split-family record not found", "Error updating record", 404)

        for key, value in split_family_data.dict(exclude_unset=True).items():
            setattr(split_family, key, value)

        db.commit()
        db.refresh(split_family)
        return SUCCESS_RESPONSE(split_family, "Split-family record updated successfully", 200)
    except Exception as e:
        db.rollback()
        return ERROR_RESPONSE(str(e), "Error updating split-family record", 500)


def fetch_split_family_by_id_model(db, split_family_id):
    try:
        split_family = db.query(SplitFamily).filter(SplitFamily.id == split_family_id).first()
        if not split_family:
            return ERROR_RESPONSE("Split-family record not found", "Error fetching record", 404)
        return SUCCESS_RESPONSE(split_family, "Split-family record fetched successfully", 200)
    except Exception as e:
        return ERROR_RESPONSE(str(e), "Error fetching split-family record", 500)


def delete_split_family_model(db, split_family_id):
    try:
        split_family = db.query(SplitFamily).filter(SplitFamily.id == split_family_id).first()
        if not split_family:
            return ERROR_RESPONSE("Split-family record not found", "Error deleting record", 404)

        db.delete(split_family)
        db.commit()
        return SUCCESS_RESPONSE(split_family, "Split-family record deleted successfully", 200)
    except Exception as e:
        db.rollback()
        return ERROR_RESPONSE(str(e), "Error deleting split-family record", 500)
