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
    result = manager.get_equities_reference_and_current_price()
    return jsonify(result)


@app.route('/countries', methods=['POST', 'GET'])
def countries():
    result = manager.get_countries()
    return jsonify(result)


@app.route('/country_performance', methods=['POST', 'GET'])
def country_performance():
    result = manager.get_country_performance()
    return jsonify(result)


@app.route('/sectors', methods=['POST', 'GET'])
def sectors():
    result = manager.get_sectors()
    return jsonify(result)


@app.route('/performance_per_equity/<symbols>', methods=['POST', 'GET'])
def performance_per_equity(symbols):
    number_of_days = config.reference_data_config['performance_for_last_n_days']
    symbols = symbols.split("&")
    result = manager.get_performance_per_equity(symbols, number_of_days)
    return jsonify(result)




@app.route('/performance/<period>', methods=['POST', 'GET'])
def performance(period):
    result = manager.get_equities_n_days_performance(int(period))    
    return jsonify(result)


@app.route('/winner/<period>', methods=['POST', 'GET'])
def winner(period):
    result = manager.get_equities_n_days_winner(int(period))
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
    return manager.user(email)


@app.route("/init")
def initialize_database():
    logging.info("Initializing Database")
    manager.initializing_database(config.reference_data_config['indices_filename'], config.reference_data_config['currencies_filename'], config.reference_data_config['country_codes_filename'])
    return "Database initialized"


@app.route("/update")
def update_equity_data():
    #logging.info("Updating equities data")
    #manager.update_equity_data()
    return "Use /update_performance_data"


@app.route("/update_performance_data")
def update_equity_performance_data():
    logging.info("Updating equities performance data")
    target_currency = config.reference_data_config['target_currency']
    n_days = config.reference_data_config['performance_for_last_n_days']
    manager.update_equity_performance_data(n_days, target_currency)
    return "Equity performance data updated"


@app.route("/update_reference_data")
def update_equity_reference_data():
    logging.info("Updating equities reference data")
    manager.update_equity_reference_data()
    return "Equity reference data updated"


@app.route("/reference_data")
def equity_reference_data():
    logging.info("Requesting equities reference data")
    result = manager.get_equity_reference_data()
    return jsonify(result)


@app.route("/performance_data")
def equity_performance_data():
    logging.info("Requesting equities performance data")
    result = manager.get_equity_reference_data()
    return jsonify(result)



@app.route("/")
def hello():
    logging.info("requested Hello World")
    return "Hello World!"




if __name__ == '__main__':
    logging.info('Start fin-mg Server')
    print("Start fin-mg Server")
    app.run(host='0.0.0.0', port=8000)