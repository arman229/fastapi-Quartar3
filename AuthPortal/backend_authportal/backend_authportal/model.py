from sqlmodel import SQLModel, Field, JSON
from typing import Optional
from datetime import datetime
 


class NewUsers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    email: str
    phone: str
    token: Optional[str] = None
    
    
class UserClass(SQLModel):
    username: str
    email: str
    password: str
    phone: str

class UserResponse(SQLModel):
    id: int
    username: str
    email: str
 
 