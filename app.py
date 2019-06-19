from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)