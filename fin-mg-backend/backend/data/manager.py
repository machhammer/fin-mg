
from data.database import fin_mongo as db
from data.models.fin_models import User

def user(username):
    _user = db.user(username)
    user = User(_user['username'], _user['password'], _user['firstName'], _user['lastName'], _user['token'])
    return user

