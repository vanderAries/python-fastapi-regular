from typing import Any, Optional
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    title: str
    detail: str
    errors: Optional[list[Any]] = None
