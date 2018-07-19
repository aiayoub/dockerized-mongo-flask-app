
from flask.json import JSONEncoder
import os
from flask import Flask, jsonify, redirect, url_for, send_from_directory
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
#------------------------------------------#

app = Flask(__name__)
<<<<<<< HEAD
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
=======
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

>>>>>>> c32baf9da18e421d7a634eb624c8c259a282f960
mongo = PyMongo(app)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.test_database
posts = db.posts
ecuDB = []

@app.route('/hello', methods=['GET'])
def hello_world():
    posts.insert_one({"name":"hello_world"})
    return jsonify("Hello World")

#------------------------------------------#
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)