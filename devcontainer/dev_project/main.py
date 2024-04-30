from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def hell():
    return {'hello':'world'}
@app.get('/city')
def hell():
    return {'City':'Lahore'}