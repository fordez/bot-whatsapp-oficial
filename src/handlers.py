from src.reply import resonseText
from src.dialogflow import sendDialogflow
from src.firestore import readData, insertData

def dataWhatsapp(data):
    try:
        payload = payloadWhatsapp(data)
        insertData('message',payload['message_id'],payload)
    except:
        print("Status OK")


def dataDialogflow(data):
        try:
            print(data)
        except:
            print("Status OK")



def payloadWhatsapp(data) -> dict:
    name_contact = data.entry[0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]
    number_contact = data.entry[0]["changes"][0]["value"]["messages"][0]["from"]
    message_id = data.entry[0]["changes"][0]["value"]["messages"][0]["id"]
    type_query = data.entry[0]["changes"][0]["value"]["messages"][0]["type"]
    
    SESSION_ID = session(name_contact, number_contact)

    if type_query == "text":
        queryText = data.entry[0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        nlp = sendDialogflow(queryText, SESSION_ID )
        resonseText(number_contact, nlp["answer"])

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

        return {
            'name_contact' : name_contact,
            'number_contact' : number_contact,
            'message_id' : message_id,
            'type_query' : type_query,
            'attachment_id': attachment_id
        }


        
def session(name_contact, number_contact):
    user_verify = readData('users', number_contact)
    if user_verify == 'No data':
        data_user={
            'name_contact': name_contact,
            'number_contact': number_contact,
        }
        insertData('users', number_contact, data_user)
        return number_contact
    else:
        return user_verify['number_contact']

