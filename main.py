import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('turnkey-slice-248713-c9c47509435a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#https://console.cloud.google.com/firestore/data/users?project=turnkey-slice-248713

collectionName='users'

doc_ref = db.collection(u'users').document(u'somename')
doc_ref.set({
	u'first':u'Shellkore',
	u'last':u'Sahu'
    
})

def readDataFromFirestore():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    return (docs)

docs = readDataFromFirestore()

for doc in docs:
	print(doc.get(u'first'))