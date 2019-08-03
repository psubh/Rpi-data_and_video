#!/usr/bin/env python

from flask import Flask, render_template,request
import datetime
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('turnkey-slice-248713-c9c47509435a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#https://console.cloud.google.com/firestore/data/users?project=turnkey-slice-248713

def putDataInFirestore(name,branch):
    doc_ref = db.collection(u'users').document(name)
    doc_ref.set({
        u'name':name,
        u'branch':branch        
    })


app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("getData.html")
        
    if request.method == 'POST':
        name = request.form['name']
        branch = request.form['branch']
        putDataInFirestore(name,branch)
        return render_template("success.html")

if __name__ == '__main__':
   app.run(debug = True)

