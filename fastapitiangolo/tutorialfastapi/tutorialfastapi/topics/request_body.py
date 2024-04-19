from fastapi import APIRouter
from tutorialfastapi.models import BioData,Language
router = APIRouter()
@router.post('/requestbody')
def request_body(BioData: BioData):
    return {"This is request body we are sending from client to the server ": BioData}

@router.post('/queryparameters')
def queryparameters(name:str,age:int,gender:str,occupation:str,language:Language):
    return {"In above function we are using the query paramerters ": f"My name is {name}and age is {age} and gender is {gender} and occupation is{occupation} and language is {language}"}
