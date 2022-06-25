import requests

TOKEN_ACESS = "EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD"
url = "https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=880415832922268&ext=1655924959&hash=ATvXU8m0Dxu3SWrrpeBFameRIn-1FTA44LCSTNzko4C5zA"

headers = {
    "Authorization":"Bearer EAAP9zDM8H2ABANpZAymzS3tZA9Ho7XyYfVZBVKRanlZBUnObZBJzfQJ3E3kZB67ITUZATZAwIknie1Ot9McrfwyeKXUH0d9hqCOkJQ0ERlgfUMITeAvTTSJSVuRZBolzcM91yLH6jrNZAJHZB3ZCHCCGcGzLxAHOiYB5vT65ZAslQ8kPzXf050GVlDYlc3ySGZBiuctBNZAYwJZBO4T0cgZDZD"
}


response = requests.get(url, headers=headers)
imagen = open("gato.jpg","wb")
imagen.write(response.content)

print(response.status_code)