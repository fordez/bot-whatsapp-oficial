import json
import requests


async def resonseText(number_contact, answer):
        url = "https://graph.facebook.com/v13.0/113727284679483/messages"

        headers = {
            "Authorization":"Bearer EAAP9zDM8H2ABANPuhrM3m4O0oWdyAGZB6juKw9VD2qU4JUlAJhhlKXrHs9mGuMDcswDbdRcKdzYiUjKAdun6UQBx1hcoca1nfOZCFQAZBDHZADnZBRQWBLznYSeqd82yl1HjKLdSWz3KZCF2hoDNrduZC7E790noKv2R1Fv6ZBpGVxbyBcLjbtZCGxxZCrwVeWy7zOjQesslWeywZDZD",
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