from flask import Flask, jsonify, request, session, abort
import json
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from collections import namedtuple

from data import manager
from data.models.fin_models import User


app = Flask(__name__)
CORS(app)

app.debug = True
app.config['SECRET_KEY'] = 'super-secret'


currentUser: User




@app.route('/auth', methods=['POST'])
def auth():
    data = request.data
    parameters = json.loads(data)
    username = parameters['username']
    password = parameters['password']
    user = manager.user(username)
    if user and (user.password == password):
        return user.toJson()
    else:    
        abort(404, description="Resource not found")

@app.route('/user', methods=['POST'])
def user(username):
    data = request.data
    parameters = json.loads(data)
    username = parameters['username']
    return manager.user(username)



@app.route("/")
def hello():
    return "Hello World!"






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)