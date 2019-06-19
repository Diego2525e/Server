from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import flask-restplua

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)