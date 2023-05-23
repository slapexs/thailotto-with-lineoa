from fastapi import FastAPI
from main import Checklotto

checklotto_obj = Checklotto()

def CheckNumberLength(input_number:str):
    if len(input_number) < 6:
        return f"Please enter all 6 numbers {6 - len(input_number)} more missing"
    elif len(input_number) > 6:
        return f"Sorry your number's more than 6 unit"
    else:
        return True
        
app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hi every body if you want to read document please go to /redoc"}

@app.get('/latest/{input_number}')
async def Checklatest(input_number:str):
    isNumberTrue = CheckNumberLength(input_number)
    if isNumberTrue == True:
        return checklotto_obj.CheckIsWonlotto(input_number)
    else:
        return {'status': 'Number length invalid', 'message': isNumberTrue}