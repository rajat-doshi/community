from pydantic import BaseModel


class MemberType(BaseModel):
    member_id: int | None = None
    first_name: str
    last_name: str
    mobile_number: str
    gender: bool
    is_active: bool
