# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:24:09 2018

@author: Emanuel Carvalho
"""

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo


app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'Suricar'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/Suricar'
app.config['JSON_AS_ASCII'] = False


mongo = PyMongo(app)

@app.route('/rede', methods=['GET'])
def getRedeNeral():
    string = ''
    saida = []
    star = mongo.db.RedeNeural.find()
    for item in star.find():
        string = str(item)
    saida.append({'Rede': string})
    return jsonify({'result' : saida})
  
       
if __name__ == "__main__":
    app.run()   