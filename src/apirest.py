from fastapi import APIRouter, Request, Response
from src.match import matchWhatsapp, matchDialogflow
from src.models import WebhookWhatsapp, FulfillmentDialogflow

api = APIRouter()

VERYFY_TOKEN = 'fordez'


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
async def receiveData(data:WebhookWhatsapp):
    await matchWhatsapp(data)
    return Response("ok", status_code=200)

@api.post('/fulfillment-dialogflow')
async def receiveData(data:FulfillmentDialogflow):
    await matchDialogflow(data)
    return Response("ok", status_code=200)