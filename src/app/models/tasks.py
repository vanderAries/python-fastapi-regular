from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Category(str, Enum):
    work = "work"
    home = "home"


class State(str, Enum):
    active = "active"
    finished = "finished"


class TaskRequest(BaseModel):
    name: str
    description: Optional[str] = None
    category: Category
    state: State


class TaskModel(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    category: Category
    state: State
    createdAt: str
    updatedAt: str
