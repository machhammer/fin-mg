import pymongo
import pprint
import json
import pandas as pd
import config
import logging
import os

class MongoDatabase:

    host: None
    database: None
    user_collection: None
    index_collection: None

    def __init__(self):
        self.connect_to_database()

    def connect_to_database(self):
        self.host = pymongo.MongoClient(config.database_config['host'])
        self.database = self.host[config.database_config['database']]
        self.user_collection = self.database[config.database_config['user_collection']]
        self.index_collection = self.database[config.database_config['index_collection']]


    def users(self):
        results = {}
        cursor = self.user_collection.find()
        for i in cursor:
            print(type(i))
            if '_id' in i: del i['_id'] 
            results.update(i)
        return (results)

    def user(self, email):
        if not self.user_collection:
            self.connect_to_database()
        try:
            user = self.user_collection.find_one({'email': email})
            return user
        except Exception as e:
            logging.error('Exception seen: %s', e)
            raise ConnectionRefusedError(401, 'UNAUTHORIZED USER')


    def register(self, email, password, firstName, lastName):
        self.user_collection.insert_one({'email': email, 'firstName': firstName, 'lastName': lastName, 'password': password})
        return "ok"

    def indices(self):
        self.index_collection.find()


    def indices(self):
        indices = self.index_collection.aggregate([ {
                '$group': {
                    '_id': {
                        'index': '$index', 
                        'country': '$country'}}}])
        return indices


    def equities(self):
        equities = self.index_collection.find()
        return equities


    def upload_reference_data_index(self, filename):
        logging.info("uploading file: %s", filename)
        cwd = os.getcwd() + "/fin-mg-backend/backend/data/finance/" + filename
        logging.info("current directory: %s", cwd)
        df = pd.read_csv(cwd, sep=';', header=None, names=['country', 'index', 'company', 'symbol', 'sector'])
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        self.index_collection.remove()
        for index, row in df.iterrows():
            query = {'country': row['country'], 'index': row['index'], 'company': row['company'],'symbol': row['symbol'], 'sector': row['sector']}
            self.index_collection.insert_one(query)
        


if __name__ == '__main__':
    print("Database started")
