from typing import List
from pydantic import BaseModel, ConfigDict, TypeAdapter


class Type_Single_Family(BaseModel):
    family_id: int
    model_config = ConfigDict(from_attributes=True)


# 1. Create the TypeAdapter for a list of your models
Type_Family_List = TypeAdapter(List[Type_Single_Family])
