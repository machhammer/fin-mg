#!/usr/bin/env python3

from flask import Flask, jsonify, request, session, abort
from flask_api import status
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from collections import namedtuple

import json
import logging
import config

logging.basicConfig(filename=config.logging_config['file'], 
                    filemode=config.logging_config['filemode'], 
                    level=config.logging_config['level'], 
                    format=config.logging_config['format'])


from data import manager
from data.models.fin_models import User



app = Flask(__name__)
CORS(app)

app.debug = True
app.config['SECRET_KEY'] = 'super-secret'


@app.route('/auth', methods=['POST'])
def auth():
    data = request.data.decode("utf-8")
    parameters = json.loads(data)
    email = parameters['email']
    password = parameters['password']
    
    try:
        user = manager.user(email)
        if user and (user.password == password):
            return user.toJson()
    except Exception as e:
        logging.error('Exception seen: %s', e)
        return status.HTTP_503_SERVICE_UNAVAILABLE


@app.route('/user', methods=['POST'])
def user(email):
    data = request.data.decode("utf-8")
    parameters = json.loads(data)
    email = parameters['email']
    return manager.user(email)


@app.route('/register', methods=['POST'])
def register():
    data = request.data.decode("utf-8")
    parameters = json.loads(data)
    firstName = parameters['firstName']
    lastName = parameters['lastName']
    email = parameters['email']
    password = parameters['password']
    return manager.register(email, firstName, lastName, password)


@app.route('/indices', methods=['POST', 'GET'])
def indices():
    result = manager.get_indices()
    return jsonify(result)


@app.route('/equities', methods=['POST', 'GET'])
def equitites():
    result = manager.get_equities()
    return jsonify(result)


@app.route('/asset/<searchValue>', methods=['POST', 'GET'])
def asset(searchValue):
    return manager.asset(searchValue)




@app.route('/user_update', methods=['POST'])
def user_update(email):
    data = request.data
    parameters = json.loads(data)
    email = parameters['email']
    firstname = parameters['firstname']
    lastname = parameters['lastname']
    
    print(lastname)

    return manager.user(email)


@app.route("/init")
def initialize_database():
    logging.info("Initializing Database")
    manager.initializing_database(config.reference_data_config['indices_filename'])
    return "Database initialized"



@app.route("/")
def hello():
    logging.info("requested Hello World")
    return "Hello World!"




if __name__ == '__main__':
    logging.info('Start fin-mg Server')
    app.run(host='0.0.0.0', port=8000)