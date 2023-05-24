from fastapi import FastAPI, status, Request
from main import Checklotto
from pydantic import BaseModel
import requests

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
from dotenv import dotenv_values

config = dotenv_values('.env')
lineBotApi = LineBotApi(config['ACCESS_TOKEN'])
handler = WebhookHandler(config['SECRET'])

app = FastAPI()

checklotto_obj = Checklotto()

def CheckNumberLength(input_number:str):
    if len(input_number) < 6:
        return f"กรุณากรอกตัวเลขให้ครับทั้ง 6 หลักค่ะ ยังขาดอีก {6 - len(input_number)} หลักนะคะ"
    elif len(input_number) > 6:
        return f"คุณกรอกตัวเลขเกินกรุณากรอกตัวเลขแค่ 6 หลักนะคะ"
    else:
        return True
        
@app.get('/')
async def root():
    return {'message': "Hi every body if you want to read document please go to /redoc"}

def CheckLatestLotto(input_number:str):
    isNumberTrue = CheckNumberLength(input_number)
    if isNumberTrue == True:
        return checklotto_obj.CheckIsWonlotto(input_number)
    else:
        return {'status': 'Number length invalid', 'message': isNumberTrue, 'sticker': {'package_id': "6325", 'sticker_id': "10979922"}}

@app.post("/latest")
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
    resultLotto = CheckLatestLotto(event.message.text)
    lineBotApi.reply_message(
        event.reply_token,
        [TextSendMessage(text=resultLotto['message']), StickerSendMessage(package_id=resultLotto['sticker']['package_id'], sticker_id=resultLotto['sticker']['sticker_id'])]
    )