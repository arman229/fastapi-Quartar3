from sqlmodel import SQLModel, Field, JSON
from typing import Optional
from datetime import datetime
 


class NewUsers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str
    password: str
    email: str
    phone: str
    token: Optional[str] = None

 