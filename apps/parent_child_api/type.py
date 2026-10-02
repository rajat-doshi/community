from pydantic import BaseModel


class ParentChildType(BaseModel):
    parent_child_id: int | None = None
    father_id: int
    mother_id: int
    child_id: int
    is_active: bool = True
