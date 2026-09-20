import sys
from pathlib import Path
from pydantic import BaseModel
from typing import Generic, TypeVar
from typing import Any

# Add root to path with alias
root = Path(__file__).parent.parent
sys.path.insert(0, str(root))

T = TypeVar("T")


class TYPE_SUCCESS_RESPONSE(BaseModel, Generic[T]):
    success: bool = True
    data: T
    msg: str | None = None
    status: int | None = None


class TYPE_ERROR_RESPONSE(BaseModel, Generic[T]):
    success: bool = False
    data: T
    msg: str | None = None
    status: int | None = None


def SUCCESS_RESPONSE(data: Any, msg: str, status_code: int) -> TYPE_SUCCESS_RESPONSE[T]:
    return {"success": True, "data": data, "msg": msg, "status": status_code}


def ERROR_RESPONSE(data: Any, msg: str, status_code: int) -> TYPE_ERROR_RESPONSE[T]:
    return TYPE_ERROR_RESPONSE(success=False, data=data, msg=msg, status=status_code)
