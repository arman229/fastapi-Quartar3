from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hell():
    return {'hello': ' world'}


 
@app.get('/compose')
def helly():
    return {'Topic': 'Compose'}


 