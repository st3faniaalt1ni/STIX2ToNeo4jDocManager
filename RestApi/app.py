from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
# app.secret_key = "secret key"

app.config["MONGO_URI"] = "mongodb://localhost:27018/threat_reports"
#app.config["MONGO_URI"] ="mongodb://localhost:27018/your_mongodb_name"

mongo = PyMongo(app)


