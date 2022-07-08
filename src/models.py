from typing import Any, List
from pydantic import BaseModel

class WebhookWhatsapp(BaseModel):
    entry: object

class FulfillmentDialogflow(BaseModel):
    queryResult: object
