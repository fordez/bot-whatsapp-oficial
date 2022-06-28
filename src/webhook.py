from fastapi import APIRouter, Request, Response
from typing import Any, List
from pydantic import BaseModel
from src.dialogflowNlp import sendDialogflow
import uuid

api = APIRouter()

VERYFY_TOKEN = 'fordez'
SESSION_ID = uuid.uuid4()



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
    name_contacts = request.entry[0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]
    number_contacts = request.entry[0]["changes"][0]["value"]["messages"][0]["from"]
    message_id = request.entry[0]["changes"][0]["value"]["messages"][0]["id"]
    type_query = request.entry[0]["changes"][0]["value"]["messages"][0]["type"]
    print(name_contacts, number_contacts, message_id, type_query )
    
    type_q = type_query

    match type_q:
        case "text":
            query = request.entry[0]["changes"][0]["value"]["messages"][0]["text"]["body"]
            print(query)
            nlp = sendDialogflow(query,123456)
            print(nlp)
        case "image":
            image_id = request.entry[0]["changes"][0]["value"]["messages"][0]["image"]["id"]
            print(image_id)
        case "audio":
            audio_id = request.entry[0]["changes"][0]["value"]["messages"][0]["audio"]["id"]
            print(audio_id)
        case "video":
            video_id = request.entry[0]["changes"][0]["value"]["messages"][0]["video"]["id"]
            print(video_id)
        case "document":
            document_id = request.entry[0]["changes"][0]["value"]["messages"][0]["document"]["id"]
            print(document_id)
        case "location":
            latitude = request.entry[0]["changes"][0]["value"]["messages"][0]["location"]["latitude"]
            longitude = request.entry[0]["changes"][0]["value"]["messages"][0]["location"]["longitude"]
            print(latitude, longitude)  
                 
    return Response("ok", status_code=200)