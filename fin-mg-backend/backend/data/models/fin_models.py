import json


class User(object):
    def __init__(self, email, password, firstName, lastName, token):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.token = token

    def __str__(self):
        return "User(id='%s')" % self.token

    def toJson(self):
        return json.dumps ({
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'token': self.token
            })

class Index(object):
    def __init__(self, country, index):
        self.country = country
        self.index = index

    def __str__(self):
        return "Index(id='%s')" % self.index

    def toJson(self):
        return json.dumps ({
            'country': self.country,
            'index': self.index
            })


class Asset(object):
    def __init__(self, symbol, high, low, open, close, volume, adj_close):
        self.symbol = symbol
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume
        self.adj_close = adj_close

    def __str__(self):
        return "Asset(symbol='%s')" % self.symbol

    def toJson(self):
        return json.dumps ({
            'symbol': self.symbol,
            'high': self.high,
            'low': self.low,
            'open': self.open,
            'close': self.open,
            'volume': self.volume,
            'adj_close': self.adj_close,
            })