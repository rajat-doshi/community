from my_database.model.parent_child import ParentChild
from shared_core.utility.api_response import (
    SUCCESS_RESPONSE,
    ERROR_RESPONSE,
)


def fetch_parent_children_list(db):
    try:
        parent_children = db.query(ParentChild).all()
        return SUCCESS_RESPONSE(parent_children, "Parent-child records fetched successfully", 200)
    except Exception as e:
        print(f"Error fetching parent-child records: {e}")
        return ERROR_RESPONSE(str(e), "Error fetching parent-child records", 500)


def create_parent_child_model(db, parent_child_data):
    try:
        new_parent_child = ParentChild(**parent_child_data.dict())
        db.add(new_parent_child)
        db.commit()
        db.refresh(new_parent_child)
        return SUCCESS_RESPONSE(new_parent_child, "Parent-child record created successfully", 201)
    except Exception as e:
        return ERROR_RESPONSE(str(e), "Error creating parent-child record", 500)


def update_parent_child_model(db, parent_child_data):
    try:
        parent_child = (
            db.query(ParentChild)
            .filter(ParentChild.parent_child_id == parent_child_data.parent_child_id)
            .first()
        )
        if not parent_child:
            return ERROR_RESPONSE(
                "Parent-child record not found", "Error updating parent-child record", 404
            )

        for key, value in parent_child_data.dict(exclude_unset=True).items():
            setattr(parent_child, key, value)

        db.commit()
        db.refresh(parent_child)
        return SUCCESS_RESPONSE(parent_child, "Parent-child record updated successfully", 200)
    except Exception as e:
        print(f"Error updating parent-child record: {e}")
        return ERROR_RESPONSE(str(e), "Error updating parent-child record", 500)


def fetch_parent_child_by_id_model(db, parent_child_id):
    try:
        parent_child = (
            db.query(ParentChild).filter(ParentChild.parent_child_id == parent_child_id).first()
        )
        if not parent_child:
            return ERROR_RESPONSE(
                "Parent-child record not found", "Error fetching parent-child record", 404
            )
        return SUCCESS_RESPONSE(parent_child, "Parent-child record fetched successfully", 200)
    except Exception as e:
        print(f"Error fetching parent-child record: {e}")
        return ERROR_RESPONSE(str(e), "Error fetching parent-child record", 500)
