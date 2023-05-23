from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': "Hi every body if you want to read document please go to /redoc"}


@app.get('/latest')
async def Checklatest():
    return 'hi'