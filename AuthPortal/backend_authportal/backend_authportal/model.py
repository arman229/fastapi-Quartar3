from sqlmodel import SQLModel, Field, JSON
from typing import Optional
from datetime import datetime
from enum import Enum
from typing import List


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    password: str
    email: str
    phone: str
    token: Optional[str] = None


class Status(str, Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'


class Priority(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'


class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    date: datetime
    status: Status
    priority: Priority
    labels: List[str] = Field(sa_type=JSON)
