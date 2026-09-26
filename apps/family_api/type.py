from typing import List
from pydantic import BaseModel, ConfigDict


class Type_Single_Family(BaseModel):
    family_id: int
    model_config = ConfigDict(from_attributes=True)


Type_Family_List = List[Type_Single_Family]
