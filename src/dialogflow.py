import os
import uuid
from google.cloud import dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'keys.json'

SESSION_ID = uuid.uuid4()

def intent(text, DIALOGFLOW_LANGUAGE_CODE, SESSION_ID, DIALOGFLOW_PROJECT_ID):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    print(SESSION_ID)

intent("hola como estas","es",SESSION_ID,"storied-reserve-350000")
