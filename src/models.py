from typing import Any, List
from pydantic import BaseModel

class WebhookWhatsapp(BaseModel):
    entry: object

class FulfillmentDialogflow(BaseModel):
    queryResult: object

class DataWhatsapp(BaseModel):
    name_contacts: str
    number_contacts: str
    message_id: str
    type_query: str

class QueryText(BaseModel):
    query: str

class Attachment(BaseModel):
    attachment_id: str

class PayloadText(BaseModel):
    dataWhatsapp: DataWhatsapp
    queryTex: QueryText

class PayloadAttachment(BaseModel):
    dataWhatsapp: DataWhatsapp
    attachment: Attachment