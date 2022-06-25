import json
import requests

TOKEN_ACESS = "EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD"
url = "https://graph.facebook.com/v13.0/113727284679483/messages"

headers = {
    "Authorization":"Bearer EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD",
    "Content-Type": "application/json"
}
datos = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "573004123821",
    "type": "text",
    "text": {
        "body": "como"
  }
}

response = requests.post(url, data=json.dumps(datos), headers=headers)


print(response.text)