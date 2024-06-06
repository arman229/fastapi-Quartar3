from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hell():
    return {'hello': 'compose'}


 
@app.get('/compose')
def helly():
    return {'Topic': 'Compose'}


 