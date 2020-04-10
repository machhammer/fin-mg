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
    currency_collection: None
    equity_collection: None
    equity_performance_collection: None
    equity_reference_collection: None
    country_codes_collection: None

    def __init__(self):
        self.connect_to_database()

    def connect_to_database(self):
        self.host = pymongo.MongoClient(config.database_config['host'])
        self.database = self.host[config.database_config['database']]
        self.user_collection = self.database[config.database_config['user_collection']]
        self.index_collection = self.database[config.database_config['index_collection']]
        self.currency_collection = self.database[config.database_config['currency_collection']]
        self.equity_collection = self.database[config.database_config['equity_collection']]
        self.equity_performance_collection = self.database[config.database_config['equity_performance_collection']]
        self.equity_reference_collection = self.database[config.database_config['equity_reference_collection']]
        self.equity_rates_collection = self.database[config.database_config['equity_rates_collection']]
        self.equity_statistics_collection = self.database[config.database_config['equity_statistics_collection']]
        self.currency_rates_collection = self.database[config.database_config['currency_rates_collection']]
        self.country_codes_collection = self.database[config.database_config['country_codes_collection']]
        
        


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



    def indices_equities(self):
        return self.index_collection.find()


    def currencies(self):
        return self.currency_collection.find()


    def indices(self):
        indices = self.index_collection.aggregate([ {
                '$group': {
                    '_id': {
                        'index': '$index', 
                        'country': '$country'}}}])
        return indices



    def get_equities(self):
        #equities = self.index_collection.find({"index": "DAX"})
        equities = self.index_collection.find({ })
        return equities

    def get_country_codes(self):
        country_codes = self.country_codes_collection.find({ }, { '_id': 0 })
        return country_codes


    def get_index_details_of_equity(self, equity_symbol):
        index = self.index_collection.find_one ({ 'symbol': equity_symbol  }, { '_id': 0 })
        return index

    def get_equities_performance_data_last_n_days(self, last_n_days):
        performance = self.equity_performance_collection.find({}, { '_id': 0
            }).sort("Date", pymongo.DESCENDING).limit(last_n_days)
        return performance

    def get_equities_rates_data_last_n_days(self, last_n_days):
        performance = self.equity_rates_collection.find({}, { '_id': 0
            }).sort("Date", pymongo.DESCENDING).limit(last_n_days)
        return performance


    def get_equities_performance_data(self, start, end):
        performance = self.equity_reference_collection.find({  }, { 
            'country': 1,
            'index': 1,
            'company': 1,
            'symbol': 1,
            'sector': 1,            
            '_id': 0})
        return performance
    
    
    def get_equities_reference_data(self):
        performance = self.equity_reference_collection.find({  }, { 
            'country': 1,
            'index': 1,
            'company': 1,
            'symbol': 1,
            'sector': 1,            
            '_id': 0})
        return performance



    def upload_reference_data_index(self, index_filename, currency_filename, country_code_filename):
        
        #UPLOAD INDEX/EQUITY FILE

        logging.info("uploading INDEX file: %s", index_filename)
        cwd = os.getcwd() + "/fin-mg-backend/backend/data/finance/" + index_filename
        logging.info("current directory: %s", cwd)
        df = pd.read_csv(cwd, sep=';', header=None, names=['country', 'index', 'symbol', 'company', 'sector'])
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        self.index_collection.remove()
        for index, row in df.iterrows():
            query = {'country': row['country'], 'index': row['index'], 'company': row['company'],'symbol': row['symbol'], 'sector': row['sector']}
            self.index_collection.insert_one(query)
        logging.info("Upload of INDEX data finished!")

        #UPLOAD INDEX/CURRENCY FILE

        logging.info("uploading CURRENCY file: %s", currency_filename)
        cwd = os.getcwd() + "/fin-mg-backend/backend/data/finance/" + currency_filename
        logging.info("current directory: %s", cwd)
        df = pd.read_csv(cwd, sep=';', header=None, names=['index', 'currency'])
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        self.currency_collection.remove()
        for index, row in df.iterrows():
            query = {'index': row['index'], 'currency': row['currency']}
            self.currency_collection.insert_one(query)
        logging.info("Upload of CURRENCY data finished!")

        #COUNTRY CODE FILE

        logging.info("uploading COUNTRY CODES file: %s", country_code_filename)
        cwd = os.getcwd() + "/fin-mg-backend/backend/data/finance/" + country_code_filename
        logging.info("current directory: %s", cwd)
        df = pd.read_csv(cwd, sep=';', header=None, names=['country', 'code'])
        df.reset_index(inplace=True)
        data_dict = df.to_dict("records")
        self.country_codes_collection.remove()
        for index, row in df.iterrows():
            query = {'country': row['country'], 'code': row['code']}
            self.country_codes_collection.insert_one(query)
        logging.info("Upload of COUNTRY CODES data finished!")


    def regenerate_equity_collection(self, equities_dataframe):
        logging.info("Remove equity collection")
        self.equity_collection.remove()
        logging.info("Insert updated equity collection")
        self.equity_collection.insert_many(equities_dataframe.to_dict('records'))
        logging.info("Regenaration of equity collection finished!")

    '''
    def regenerate_equity_performance_collection(self, equity_performance_dataframe):
        logging.info("Remove equity performance collection")
        self.equity_performance_collection.remove()
        logging.info("Insert updated equity performance collection")    
        self.equity_performance_collection.insert_many(equity_performance_dataframe.to_dict('records'))
        logging.info("Regenaration of equity collection finished!")
    '''

    def regenerate_equity_reference_collection(self, equity_reference_data):
        logging.info("Remove equity reference data collection")
        self.equity_reference_collection.remove()
        logging.info("Insert updated equity reference data collection")    
        self.equity_reference_collection.insert_many(equity_reference_data.to_dict('records'))
        logging.info("Regenaration of equity reference data collection finished!")


    def regenerate_equity_performance_collection(self, equity_performance_data):
        logging.info("Remove equity performance data collection")
        self.equity_performance_collection.remove()
        logging.info("Insert updated equity performance data collection")    
        self.equity_performance_collection.insert_many(equity_performance_data.to_dict('records'))
        logging.info("Regenaration of equity performance data collection finished!")


    def regenerate_equity_rates_collection(self, equity_rates):
        logging.info("Remove equity rates collection")
        self.equity_rates_collection.remove()
        logging.info("Insert updated equity rates collection")    
        self.equity_rates_collection.insert_many(equity_rates.to_dict('records'))
        logging.info("Regenaration of equity rates collection finished!")


    def regenerate_equity_statistics_collection(self, equity_statistics):
        logging.info("Remove equity statistics collection")
        self.equity_statistics_collection.remove()
        logging.info("Insert updated equity statistics collection")    
        self.equity_statistics_collection.insert_many(equity_statistics.to_dict('records'))
        logging.info("Regenaration of equity statistics collection finished!")

    def regenerate_currency_rates_collection(self, currency_rates):
        logging.info("Remove currency rates collection")
        self.currency_rates_collection.remove()
        logging.info("Insert updated currency rates collection")    
        self.currency_rates_collection.insert_many(currency_rates.to_dict('records'))
        logging.info("Regenaration of currency rates collection finished!")



if __name__ == '__main__':
    print("Database started")
