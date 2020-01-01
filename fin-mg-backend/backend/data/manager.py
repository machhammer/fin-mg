
from data.database.fin_mongo import MongoDatabase
from data.finance import fin_finance as fin
from data.models.fin_models import User, Index


import logging

db = MongoDatabase()

def user(email):
    logging.info('get user data for email: %s', email)
    try:
        _user = db.user(email)
        user = User(_user['email'], _user['password'], _user['firstName'], _user['lastName'], str(_user.get('_id')))
        return user
    except Exception as e:
        logging.error('Exception seen: %s', e)
        raise e

def register(email, firstName, lastName, password):
    return db.register(email, password, firstName, lastName)
    

def get_indices():
    indices = db.indices()
    indices_list = []
    for index in indices:
        index_dict = {
            'index': index['_id']['index'], 
            'country': index['_id']['country']
        }
        indices_list.append(index_dict)
    return indices_list


def get_equities():
    equities = db.equities()
    equities_list = []
    for equity in equities:
        prices = fin.get_price_for_equity(equity['symbol'])
        print(prices)
        equity_dict = {
            'index': equity['index'], 
            'country': equity['country'],
            'company': equity['company'],
            'symbol': equity['symbol'],
            'sector': equity['sector'],
        }
        equities_list.append(equity_dict)
    return equities_list



def asset(searchValue):
    return fin.asset(searchValue).to_json()

def initializing_database(reference_data_index_file):
    logging.info(reference_data_index_file)
    db.upload_reference_data_index(reference_data_index_file)


def load_news_data():
    print ("load")

if __name__ == '__main__':
    print("Manager started")