import pandas as pd
from pandas_datareader import data as pdr
import yfinance as fyf
import datetime
import logging
from data.database.fin_mongo import MongoDatabase
import time

db = MongoDatabase()

fyf.pdr_override()

class FinanceModule:

    def asset(self, searchValue):
        search = pdr.get_data_yahoo(searchValue, 
                            start=datetime.datetime(2019, 9, 2), 
                            end=datetime.datetime(2019, 9, 6))
        return search

    def get_price_for_equity(self, equity_symbol):
        print("sarch for: " + equity_symbol)
        search = pdr.get_data_yahoo(equity_symbol, 
                            start=datetime.datetime(2019, 12, 27), 
                            end=datetime.datetime(2019, 12, 27))
        return search.to_json(orient='records')


    def get_countries(self):
        indices = db.indices_equities()
        countries = pd.DataFrame(indices)
        countries = countries["country"]
        countries = countries.drop_duplicates()
        countries = countries.sort_values()
        return countries.values.tolist()

    def get_sectors(self):
        reference_data = db.get_equities_reference_data()
        sectors = pd.DataFrame(reference_data)
        sectors = sectors["sector"]
        sectors = sectors.drop_duplicates()
        sectors = sectors.sort_values()
        return sectors.values.tolist()


    def get_country_performance(self):
        country_df = pd.DataFrame(db.get_country_codes())
        country_df['performance']=0
        country_df = country_df.sort_values(by=['code'], ascending=False)
        return country_df.to_dict('records')


    def get_equity_performance_data (self, list_of_equity_symbols, start, end):
        data = pdr.get_data_yahoo(stocks, start = start, end = end)
        return data


    def get_equity_detail_data (self, equity_symbol):
        detail_info = None #fyf.Ticker(equity_symbol)
        return detail_info

    def get_performance_per_equity(self, symbols, last_n_days):
        performance_data = db.get_equities_performance_data_last_n_days(last_n_days)
        performance_df = pd.DataFrame(performance_data)
        performance_df = performance_df[performance_df.columns.intersection(symbols)]
        performance_df['Date'] = performance_df['Date'].astype('int64') / int(1e6)
        performance_df = performance_df.sort_values(by=['Date'], ascending=True)

        return performance_df.dropna().values.tolist()


    def get_equity_performance_over_last_n_days(self, last_n_days):
        reference_data = db.get_equities_reference_data()
        reference_df = pd.DataFrame(reference_data)
        reference_df = reference_df.set_index('symbol')
        performance_data = db.get_equities_performance_data_last_n_days(last_n_days)
        performance_df = pd.DataFrame(performance_data)
        performance_df.columns = performance_df.columns.map(lambda n: n.replace("_", "."))
        performance_df = performance_df.set_index('Date')
        rates_df = ((1-(performance_df/performance_df.shift(last_n_days-1)))*100).tail(1)
        rates_df = rates_df.T
        rates_df = rates_df.rename(columns={rates_df.columns[0]: 'performance'})
        rates_df = rates_df.rename_axis(None, axis=1).rename_axis('symbol', axis=0)
        rates_df = rates_df[rates_df['performance'] > -1000]
        rates_df = rates_df.join(reference_df)
        rates_df = rates_df.sort_values(by=['performance'], ascending=False)
        rates_df = rates_df.reset_index()

        return rates_df.to_dict('records')


    def get_equities_current_performance(self):
        
        reference_data = db.get_equities_reference_data()
        reference_df = pd.DataFrame(reference_data)
        reference_df = reference_df.set_index('symbol')

        rates_data = db.get_equities_rates_data_last_n_days(1)
        rates_df = pd.DataFrame(rates_data)
        rates_df = rates_df.set_index('Date')
        rates_df.columns = rates_df.columns.map(lambda n: n.replace("_", "."))
        rates_df = rates_df.T
        rates_df = rates_df.rename(columns={rates_df.columns[0]: 'performance'})
        rates_df = rates_df.rename_axis(None, axis=1).rename_axis('symbol', axis=0)
        rates_df = rates_df[rates_df['performance'] > -1000]
        rates_df = rates_df[rates_df['performance'] < 1000]
        
        rates_df = rates_df.join(reference_df)
        rates_df = rates_df.sort_values(by=['performance'], ascending=False)
        rates_df = [rates_df.head(20), rates_df.tail(20)]
        rates_df = pd.concat(rates_df)
        rates_df = rates_df.reset_index()
        
        return rates_df.to_dict('records')




    def get_equities_reference_and_current_price(self):
        
        reference_data = db.get_equities_reference_data()
        reference_df = pd.DataFrame(reference_data)
        reference_df = reference_df.set_index('symbol')
        
        performance_data = db.get_equities_performance_data_last_n_days(1)
        performance_df = pd.DataFrame(performance_data)
        performance_df = performance_df.set_index('Date')
        performance_df.columns = performance_df.columns.map(lambda n: n.replace("_", "."))
        performance_df = performance_df.T
        performance_df = performance_df.rename(columns={performance_df.columns[0]: 'current_price'})
        performance_df = performance_df.rename_axis(None, axis=1).rename_axis('symbol', axis=0)

        rates_data = db.get_equities_rates_data_last_n_days(1)
        rates_df = pd.DataFrame(rates_data)
        rates_df = rates_df.set_index('Date')
        rates_df.columns = rates_df.columns.map(lambda n: n.replace("_", "."))
        rates_df = rates_df.T
        rates_df = rates_df.rename(columns={rates_df.columns[0]: 'performance'})
        rates_df = rates_df.rename_axis(None, axis=1).rename_axis('symbol', axis=0)

        result_df = reference_df.join(performance_df)
        result_df = result_df.join(rates_df)
        
        result_df = result_df.reset_index()
        result_df = result_df.sort_values(by=['index', 'company'])

        #result_df = result_df.iloc[427:428]
        result_df = result_df.fillna(0)

        return result_df.to_dict('records')

    
    
    def generate_equities_performance_data (self, list_of_equity_symbols, start, end, target_currency):
        
        #Load PERMANCE data
        logging.info("Loading Equity Performance Data")
        list_of_equity_symbols = list(set(list_of_equity_symbols))
        equity_performance_data = pd.DataFrame()
        length = len(list_of_equity_symbols)
        batch_size = 30
        nr_batches = round(length/batch_size + 0.5)
        
        count = 0
        batch_count = 1
        while (count < length):
            end_batch = count + batch_size
            if (end_batch > length):
                end_batch = length
            print("batch " + str(batch_count) + " from " + str(nr_batches))
            
            data = pdr.get_data_yahoo(list_of_equity_symbols[count:end_batch], start = start, end = end)['Adj Close']
            time.sleep(10)

            if (count==0):
                equity_performance_data = data
            else:
                equity_performance_data = equity_performance_data.join(data)

            count += batch_size
            batch_count += 1
            
        
        equity_performance_data = equity_performance_data.fillna(method='ffill')
        equity_performance_data.columns = equity_performance_data.columns.map(lambda n: n.replace("_", "."))
        equity_performance_data  = equity_performance_data.reset_index()
        equity_performance_data = equity_performance_data.set_index('Date')

        #Convert to target currency
        logging.info("Loading Currencies from DB")
        currencies = pd.DataFrame(db.currencies()).set_index('index')
        del currencies['_id']

        logging.info("Loading Indices from DB")
        indices = pd.DataFrame(db.indices_equities())
        indices = indices[['index', 'symbol']]
        indices = indices.set_index('index')

        logging.info("Join Indices and Currencies from DB")
        index_currency = currencies.join(indices)
        index_currency['currency_conversion_symbol'] = index_currency['currency'] + target_currency + '=X'

        logging.info("Loading Currency Performance Data")
        currency_conversion_symbols = index_currency['currency_conversion_symbol'].drop_duplicates().values.tolist()
        currency_conversion_rates = pdr.get_data_yahoo(currency_conversion_symbols, start = start, end = end)
        currency_conversion_rates = currency_conversion_rates['Adj Close']
        currency_conversion_rates = currency_conversion_rates.fillna(1)

        currency_performance_data = pd.DataFrame().reindex_like(equity_performance_data)
        

        currency_performance_data = currency_performance_data.apply(lambda x: currency_conversion_rates[index_currency.loc[index_currency['symbol'] == x.name].tail(1)['currency_conversion_symbol'].values[0]], axis=0)

        logging.info("Calculate new Performance Data")
        equity_performance_data = equity_performance_data * currency_performance_data
        
        
        #Calulate daily returns
        logging.info("Calculate Daily Rates")
        equity_rates = (-1)*(1-( equity_performance_data / equity_performance_data.shift(1) ))*100
        equity_rates = equity_rates.reset_index()

        #Calulate statistics
        logging.info("Calculate Statistics")
        equity_statistics = equity_rates.describe()
        equity_statistics = equity_statistics.reset_index()

        equity_performance_data = equity_performance_data.reset_index()

        logging.info("Prepare data for storing in MongoDB")
        equity_performance_data.columns = equity_performance_data.columns.map(lambda n: n.replace(".", "_"))
        equity_rates.columns = equity_rates.columns.map(lambda n: n.replace(".", "_"))
        equity_statistics.columns = equity_statistics.columns.map(lambda n: n.replace(".", "_"))
        currency_conversion_rates.columns = currency_conversion_rates.columns.map(lambda n: n.replace(".", "_"))

        return [equity_performance_data, equity_rates, equity_statistics, currency_conversion_rates]
        
        

    def generate_equities_reference_data (self, list_of_equity_symbols):
        
        equities_reference_data = pd.DataFrame()
        for equity in list_of_equity_symbols:
            logging.info("get data for %s " % equity)
            equity_detail_info = self.get_equity_detail_data(equity)
            index_info = db.get_index_details_of_equity(equity)
            
            equity_row = {'company': index_info['company'], 'index': index_info['index'], 'country': index_info['country'], 'symbol': index_info['symbol'], 'sector': index_info['sector'], 
                    'symbol': index_info['symbol']}
            try:
                equity_row.update(equity_detail_info.info)
            except:
                logging.info("problem with equity: %s" % equity)
            equities_reference_data = equities_reference_data.append(equity_row, ignore_index=True)
            #time.sleep(5)
        return equities_reference_data