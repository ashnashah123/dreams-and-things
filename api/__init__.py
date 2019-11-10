from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'dreams'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dreams'

mongo = PyMongo(app)