import json
import requests


async def resonseText(number_contact, answer):
        url = "https://graph.facebook.com/v13.0/113727284679483/messages"

        headers = {
            "Authorization":"Bearer EAAP9zDM8H2ABAPrZAgSS2GIRTbRk4a0S9stIJZAmQRSDUzMI7DLSu9AdS8z6Q8ZAzj1QDURJH2Ue2m9lZA93R9a0gdIOoltg5tZBBvVHOGyUUyLFdUCxVXFEcZBgQ8Deaa1fgryKZAmrhFE8wRmYLVjxz5e2wZBZBsxhM6GQDZB9dKcDwosHocj7CHtZBUBpsh4EU13bKehxmoU0AZDZD",
            "Content-Type": "application/json"
        }

        datos = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number_contact,
            "type": "text",
            "text": {
                "body": answer
            }
        }

        response = requests.post(url, data=json.dumps(datos), headers=headers)
        print(response.text)


async def obtenerMedios():
        url = "https://graph.facebook.com/v13.0/880415832922268"

        headers = {
            "Authorization":"Bearer EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD"
        }

        response = requests.get(url, headers=headers)
        print(response.text)


async def descargarMedios():

    url = "https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=880415832922268&ext=1655924959&hash=ATvXU8m0Dxu3SWrrpeBFameRIn-1FTA44LCSTNzko4C5zA"

    headers = {
        "Authorization":"Bearer EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD"
    }

    response = requests.get(url, headers=headers)
    imagen = open("gato.jpg","wb")
    imagen.write(response.content)

    print(response.status_code)