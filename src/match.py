
import uuid
from src.handlers import payloadWhatsapp
from src.reply import resonseText
from src.firestore import readData, insertData

async def matchWhatsapp(data):
    try:
        payload = await payloadWhatsapp(data)
        print(payload)
        user_verify = await readData('users', payload['number_contact'])
        if user_verify.exists:
            SESSION_ID = user_verify['SESSION_ID']
            print('si')
        else:
            SESSION_ID = uuid.uuid4()
            print('hola')
            data_user={
                    'name_contact': payload['name_contact'],
                    'number_contact': payload['number_contact'],
                    'SESSION_ID' : SESSION_ID,
                }
            await insertData('users', payload['number_contact'], data_user)
        
        
        await resonseText(payload['number_contacts'], payload["answer"])
    except:
        print("Status OK")


async def matchDialogflow(data):
        try:
            print(data)
        except:
            print("Status OK")