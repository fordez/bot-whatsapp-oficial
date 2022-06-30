import os
from google.cloud import dialogflow
from src.reply import resonseText

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'keysbot.json'
PROJECT_ID = "storied-reserve-350000"
LANGUAGE_CODE = "es"

async def sendDialogflow(number_contacts,text,SESSION_ID):
    
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(PROJECT_ID, SESSION_ID)
        text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        #print(response.query_result.fulfillment_text)
        await resonseText(number_contacts,response.query_result.fulfillment_text)
    
