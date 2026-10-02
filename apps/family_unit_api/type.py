from pydantic import BaseModel


class FamilyUnitType(BaseModel):
    family_unit_id: int | None = None
    family_name: str
    is_active: bool = True
