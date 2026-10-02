from my_database.model.family_units import FamilyUnits
from shared_core.utility.api_response import (
    SUCCESS_RESPONSE,
    ERROR_RESPONSE,
)


def fetch_family_units_list(db):
    try:
        family_units = db.query(FamilyUnits).all()
        return SUCCESS_RESPONSE(family_units, "Family units fetched successfully", 200)
    except Exception as e:
        print(f"Error fetching family units: {e}")
        return ERROR_RESPONSE(str(e), "Error fetching family units", 500)


def create_family_unit_model(db, family_unit_data):
    try:
        new_family_unit = FamilyUnits(**family_unit_data.dict())
        db.add(new_family_unit)
        db.commit()
        db.refresh(new_family_unit)
        return SUCCESS_RESPONSE(new_family_unit, "Family unit created successfully", 201)
    except Exception as e:
        return ERROR_RESPONSE(str(e), "Error creating family unit", 500)


def update_family_unit_model(db, family_unit_data):
    try:
        family_unit = (
            db.query(FamilyUnits)
            .filter(FamilyUnits.family_unit_id == family_unit_data.family_unit_id)
            .first()
        )
        if not family_unit:
            return ERROR_RESPONSE("Family unit not found", "Error updating family unit", 404)

        for key, value in family_unit_data.dict(exclude_unset=True).items():
            setattr(family_unit, key, value)

        db.commit()
        db.refresh(family_unit)
        return SUCCESS_RESPONSE(family_unit, "Family unit updated successfully", 200)
    except Exception as e:
        print(f"Error updating family unit: {e}")
        return ERROR_RESPONSE(str(e), "Error updating family unit", 500)


def fetch_family_unit_by_id_model(db, family_unit_id):
    try:
        family_unit = (
            db.query(FamilyUnits).filter(FamilyUnits.family_unit_id == family_unit_id).first()
        )
        if not family_unit:
            return ERROR_RESPONSE("Family unit not found", "Error fetching family unit", 404)
        return SUCCESS_RESPONSE(family_unit, "Family unit fetched successfully", 200)
    except Exception as e:
        print(f"Error fetching family unit: {e}")
        return ERROR_RESPONSE(str(e), "Error fetching family unit", 500)
