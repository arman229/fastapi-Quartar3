from enum import Enum
from pydantic import BaseModel

class Language(str,Enum):
    urdu= 'URDU'
    punjabi= 'PUNJABI'
    hindi= 'HINDI'
    english= 'ENGLISH'
    
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None    

class BioData(BaseModel):
    name:str
    age:int
    gender:str
    occupation:str
    language:Language
        
    
    
    
    