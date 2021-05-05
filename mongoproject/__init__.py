from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MedicalData"
app.config['SECRET_KEY'] = '215b7bf6c3ada7eef97df12e699b9296'
mongo = PyMongo(app)

from mongoproject import routes