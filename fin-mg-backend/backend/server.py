import pandas as pd
import json
import pymongo
import socket

from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)


users =	{1: {
            "id": 1,
            "username": "admin",
            "password": "admin",
            "firstName": "admin",
            "lastName": "admin",
            "token": "1"
        }, 
        2: {
            "id": 2,
            "username": "user",
            "password": "user",
            "firstName": "user",
            "lastName": "user",
            "token": "1"

        }}


@app.route('/')
def hello():
    return "Hello World"

class CreateDatabase(Resource):
    def get(self):
        myclient = pymongo.MongoClient("mongodb://18.197.31.185:27017/")
        db = myclient["fin-mg-database"]
        col = db["users"]
        user = { "id": 1, "username": "admin", "password": "admin", "firstName": "admin", "lastName": "admin", "token": "t1" }
        x = col.insert_one(user)

        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname) 
        print("Your Computer IP Address is:" + IPAddr)


class User(Resource):
    def get(self):
        user =	{
            "id": 1,
            "username": "admin",
            "password": "admin",
            "firstName": "admin",
            "lastName": "admin",
            "token": "1"
        },
        return jsonify(user)


api.add_resource(User, '/user')
api.add_resource(CreateDatabase, '/createdb')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)