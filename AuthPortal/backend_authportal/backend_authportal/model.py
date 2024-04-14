from sqlmodel import SQLModel,Field


class User(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  username: str 
  password: str 
  email: str 
  mobile_number: int
  
name:str = 'arman'  
  
 
  