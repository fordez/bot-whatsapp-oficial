import uuid
from requests import session
from src.dialogflow import sendDialogflow


async def payloadWhatsapp(data) -> dict:
        name_contact = data.entry[0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]
        number_contact = data.entry[0]["changes"][0]["value"]["messages"][0]["from"]
        message_id = data.entry[0]["changes"][0]["value"]["messages"][0]["id"]
        type_query = data.entry[0]["changes"][0]["value"]["messages"][0]["type"]
        SESSION_ID = '1234567'

        if type_query == "text":
            queryText = data.entry[0]["changes"][0]["value"]["messages"][0]["text"]["body"]
            nlp = await sendDialogflow(queryText, SESSION_ID )
            return {  
                'name_contact' : name_contact,
                'number_contact' : number_contact,
                'message_id' : message_id,
                'type_query' : type_query,
                'intent': nlp['intent'],
                'queryText': queryText,
                'answer': nlp['answer']
            }
        elif type_query == 'location':
            latitude = data.entry[0]["changes"][0]["value"]["messages"][0]["location"]["latitude"]
            longitude = data.entry[0]["changes"][0]["value"]["messages"][0]["location"]["longitude"]
            print(latitude, longitude)
            return {
                    'name_contact' : name_contact,
                    'number_contact' : number_contact,
                    'message_id' : message_id,
                    'type_query' : type_query,
                    'latitude' : latitude,
                    'longitude' : longitude
        }
        else:
            attachment_id = data.entry[0]["changes"][0]["value"]["messages"][0][type_query]["id"]
            print(attachment_id)
            return {
                'name_contact' : name_contact,
                'number_contact' : number_contact,
                'message_id' : message_id,
                'type_query' : type_query,
                'attachment_id': attachment_id
        }

        
