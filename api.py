from fastapi import FastAPI, status, Request
from main import Checklotto
from pydantic import BaseModel
import requests

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import dotenv_values

config = dotenv_values('.env')
lineBotApi = LineBotApi(config['ACCESS_TOKEN'])
handler = WebhookHandler(config['SECRET'])

app = FastAPI()

class TestModel(BaseModel):
    name:str
    signature:str

checklotto_obj = Checklotto()

def CheckNumberLength(input_number:str):
    if len(input_number) < 6:
        return f"Please enter all 6 numbers {6 - len(input_number)} more missing"
    elif len(input_number) > 6:
        return f"Sorry your number's more than 6 unit"
    else:
        return True
        
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

@app.post("/webhook")
async def webhook_handler(request: Request):
    body = await request.body()
    signature = request.headers["X-Line-Signature"]
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        return "Invalid signature", 400
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    lineBotApi.reply_message(
        event.reply_token,
        TextSendMessage(text="You said: " + event.message.text)
    )

