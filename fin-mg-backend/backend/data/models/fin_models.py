import json

class User(object):
    def __init__(self, username, password, firstName, lastName, token):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.token = token

    def __str__(self):
        return "User(id='%s')" % self.username

    def toJson(self):
        return json.dumps ({
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'token': self.token
            })