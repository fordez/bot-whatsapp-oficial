import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("keysfirestore.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def insertData(colletion_id, document_id, data):
    doc_ref = db.collection(colletion_id).document(document_id).set(data)
    print('data save firestore')

def readData(collection_id, document_id ):
    doc_ref = db.collection(collection_id).document(document_id).get()
    if doc_ref.exists:
        return doc_ref.to_dict()
    else:
        return 'No data'

def deleteData():
    db.collection('users').document('datos').delete()

