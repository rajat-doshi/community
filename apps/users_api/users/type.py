from pydantic import BaseModel, ConfigDict, TypeAdapter
from typing import List


class Type_User(BaseModel):
    first_name: str
    last_name: str
    mobile_number: str
    gender: int
    is_active: int

    model_config = ConfigDict(from_attributes=True)


Type_UserList = TypeAdapter(List[Type_User])
