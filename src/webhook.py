from email import message
from urllib import response
from fastapi import APIRouter, Request, Response
from typing import Any, List
from pydantic import BaseModel

api = APIRouter()

VERYFY_TOKEN = 'fordez'




class DataRequest(BaseModel):
    entry: List = []
    

@api.get('/webhook')
async def verify(request:Request):
        try:
            if request.query_params['hub.mode'] and request.query_params['hub.verify_token']:
                if request.query_params['hub.mode'] == 'subscribe' and request.query_params['hub.verify_token'] == VERYFY_TOKEN:
                    print('WEBHOOK_VERIFIED')
                    return  Response(content=request.query_params['hub.challenge'], status_code=200)
                else:
                    return Response(content='verify token requerido ', status_code=403)
        except:
            print('NO VERIFY')
            return Response(content='verify token requerido fordez y lucy', status_code=403)        

@api.post('/webhook')
def data(request:DataRequest):

    platform = 'whatsapp'
    #number_contacts = request.entry[0]["changes"][0]["value"]["messages"][0]["from"]
    #message_id = request.entry[0]["changes"][0]["value"]["messages"][0]["id"]
    #timestamp = request.entry[0]["changes"][0]["value"]["messages"][0]["timestamp"]
    #intent = request.entry[0]["changes"][0]["value"]["messages"][0]["text"]["body"]
    #print(number_contacts, message_id, timestamp, intent )
    print(platform)

    type_intent = "text"

    match type_intent:
        case "text": print("hola fer")
    return Response("ok", status_code=200)