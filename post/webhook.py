from fastapi import APIRouter, Request, Response
from typing import Any, List
from pydantic import BaseModel

api = APIRouter()

VERYFY_TOKEN = 'fordez'




class DataRequest(BaseModel):
    object: str
    entry: List = []

@api.get('/webhook')
async def verify(request:Request):
        try:
            if request.query_params['hub.mode'] and request.query_params['hub.verify_token']:
                if request.query_params['hub.mode'] == 'subscribe' and request.query_params['hub.verify_token'] == VERYFY_TOKEN:
                    print('WEBHOOK_VERIFIED')
                    return Response(content=request.query_params['hub.challenge'], status_code=200)
                else:
                    return Response(content='verify token requerido', status_code=403)
        except:
            print('NO VERIFY')
            return Response(content='verify token requerido', status_code=403)        

@api.post('/webhook')
def data(response:DataRequest):
    print(response.object)
    return Response("ok", status_code=200)