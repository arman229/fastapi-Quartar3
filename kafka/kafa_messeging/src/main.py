from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hell():
    return {'hello': 'kafka messages'}


 
@app.get('/kafka')
def helly():
    return {'Topic': 'kafka'}

 