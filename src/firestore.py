from xml.dom.minidom import Document
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("keysfirestore.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

data = {
    'nombre': 'fernando',
    'apellido': 'ordoñez',
    'año': 1992
}

colletion = "users"
document = "datos"

def insertData(colletion, document, data):
    doc_ref = db.collection(colletion).document(document).set(data)

def readData():
    doc_ref = db.collection('users').document('datos').get()
    if doc_ref.exists:
        return doc_ref.to_dict()
    else:
        return 'No such document!'

def deleteData():
    db.collection('users').document('datos').delete()

resultado = readData()
print(resultado)