from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hell():
    return {'hello': 'world'}


@app.get('/city')
def helly():
    return {'City': 'Lahore'}


@app.get('/country')
def country():
    return {'Country': 'pakistansdfasdfas'}
