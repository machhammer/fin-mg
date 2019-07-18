import pandas as pd
import json

from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)



@app.route('/')
def hello():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)