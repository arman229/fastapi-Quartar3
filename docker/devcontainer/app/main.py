from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hell():
    return {'hello': ' new world'}


@app.get('/city')
def helly():
    return {'City': 'Lahore'}
@app.get('/devcontainer')
def helly():
    return {'Topic': 'devcontainer'}


@app.get('/country')
def country():
    return {'Country': 'pakistansdfasdfas'}
