import json
import requests


async def resonseText(number_contact, query_text):
        url = "https://graph.facebook.com/v13.0/113727284679483/messages"

        headers = {
            "Authorization":"Bearer EAAP9zDM8H2ABAP9cKwqd6GJEuJf516I221CU3kVB95BHAcU2Tx84iMIJ71B5r6fG02CGFJG0e01I0ZBlsE0Thh1UpWQnHN1ZBciGzG0Uew5lsZCmaSDs6EwOZCvor6eklJZBMvb7RGOPYmSRRtOyrkO69wBayUuhKArxZBghkhljISEqppxN3OrbOj0RkDqxaQDM6AjztL6AZDZD",
            "Content-Type": "application/json"
        }

        datos = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number_contact,
            "type": "text",
            "text": {
                "body": query_text
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