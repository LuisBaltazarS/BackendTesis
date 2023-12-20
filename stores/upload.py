import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate('path/to/key.json')
firebase_admin.initialize_app(cred)

# Load JSON data
with open('path/to/plazavea.json') as f:
    plazavea_data = json.load(f)

with open('path/to/products.json') as f:
    products_data = json.load(f)

with open('path/to/tottus.json') as f:
    tottus_data = json.load(f)

# Function to upload data to Firestore
def upload_to_firestore():
    db = firestore.client()
    db.collection('virtualStores').document('plazavea').set(plazavea_data)
    db.collection('virtualStores').document('tottus').set(tottus_data)
    db.collection('allProducts').document('products').set(products_data)

# Call the function to upload data
upload_to_firestore()
