
from data.database.fin_mongo import MongoDatabase
from data.finance.fin_finance import FinanceModule
from data.models.fin_models import User, Index
import config

from datetime import datetime, timedelta
import math
import logging
import json

db = MongoDatabase()
fin = FinanceModule()

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

def get_countries():
    countries = fin.get_countries()
    return countries

def get_sectors():
    sectors = fin.get_sectors()
    return sectors

def get_performance_per_equity(symbols, number_of_days):
    perf_data = fin.get_performance_per_equity(symbols, number_of_days)
    return perf_data


def get_equities_reference_and_current_price():
    equity_data = fin.get_equities_reference_and_current_price()
    return equity_data


def get_equities_current_performance():
    performance = fin.get_equities_current_winner()
    return performance


def get_equities_n_days_performance(last_n_days):
    performance = None
    if (last_n_days==1):
        performance = fin.get_equities_current_performance()
    else:    
        performance = fin.get_equity_performance_over_last_n_days(last_n_days)
    return performance



def get_equity_reference_data():
    equities_reference_data = db.get_equities_reference_data()
    equities_reference_list = []
    
    for equity in equities_reference_data:
        clean_dict = {}
        for key, value in equity.items():
            if (type(value) == float):
                if (math.isnan(value)):
                    value = 0
            clean_dict[key] = value        
        
        equities_reference_list.append(clean_dict)
    
    return equities_reference_list


def asset(searchValue):
    return fin.asset(searchValue).to_json()


def get_country_performance():
    return fin.get_country_performance()

def initializing_database(reference_data_index_file, index_currency_file, country_codes_file):
    logging.info(reference_data_index_file)
    logging.info(index_currency_file)
    db.upload_reference_data_index(reference_data_index_file, index_currency_file, country_codes_file)




def update_equity_data():
    equities_list = db.get_equities()
 
    equities_symbols = []
    for equity in equities_list:
        equities_symbols.append(equity['symbol'])
    logging.info("Updating performance data of %d equities" % len(equities_symbols))
    
    end = datetime.today().now()
    start = end-timedelta(days=360)
    equity_data = fin.generate_equities_performance_data(equities_symbols, start, end)
    
    db.regenerate_equity_collection(equity_data)
    

def update_equity_performance_data(load_for_n_days, target_currency):
    equities_list = db.get_equities()
 
    equities_symbols = []
    for equity in equities_list:
        equities_symbols.append(equity['symbol'])
    logging.info("Updating performance data of %d equities" % len(equities_symbols))
    
    end = datetime.today().now()
    start = end-timedelta(days=load_for_n_days)
    logging.info("Number of days to load: %d " % load_for_n_days)
    [equity_performance_data, equity_rates, equity_statistics, currency_rates] = fin.generate_equities_performance_data(equities_symbols, start, end, target_currency)

    db.regenerate_equity_performance_collection(equity_performance_data)
    db.regenerate_equity_rates_collection(equity_rates)
    db.regenerate_equity_statistics_collection(equity_statistics)
    #db.regenerate_currency_rates_collection(currency_rates)


def update_equity_reference_data():
    equities_list = db.get_equities()
 
    equities_symbols = []
    for equity in equities_list:
        equities_symbols.append(equity['symbol'])
    logging.info("Updating reference data of %d equities" % len(equities_symbols))
    
    equity_reference_data = fin.generate_equities_reference_data(equities_symbols)
    
    db.regenerate_equity_reference_collection(equity_reference_data)




def load_news_data():
    print ("load")

if __name__ == '__main__':
    print("Manager started")