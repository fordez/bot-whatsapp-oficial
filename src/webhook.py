from fastapi import APIRouter, Request, Response
from typing import Any, List
from pydantic import BaseModel
from requests import request
from src.payload import payloadWhatsapp, payloadDialogflow


api = APIRouter()

VERYFY_TOKEN = 'fordez'

class DataWhatsapp(BaseModel):
    entry: List = []

class DataDialogflow(BaseModel):
    queryResult: object
    

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
async def receive(data:DataWhatsapp):
    await payloadWhatsapp(data.entry[0])
    return Response("ok", status_code=200)

@api.post('/fulfillment-dialogflow')
async def receive(data:DataDialogflow):
        await payloadDialogflow(data.queryResult)
        return Response("ok", status_code=200)