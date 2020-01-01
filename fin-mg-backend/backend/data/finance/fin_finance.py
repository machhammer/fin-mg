import pandas_datareader as pdr
import pandas as pd
import datetime

from data.database.fin_mongo import MongoDatabase

def asset(searchValue):
    search = pdr.get_data_yahoo(searchValue, 
                          start=datetime.datetime(2019, 9, 2), 
                          end=datetime.datetime(2019, 9, 6))
    return search

def get_price_for_equity(equity_symbol):
    print("sarch for: " + equity_symbol)
    search = pdr.get_data_yahoo(equity_symbol, 
                          start=datetime.datetime(2019, 12, 27), 
                          end=datetime.datetime(2019, 12, 27))
    return search.to_json(orient='records')