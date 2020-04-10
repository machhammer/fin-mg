
import logging


logging_config = {
            'file': 'server.log',
            'filemode': 'w',
            'level': logging.INFO,
            'format': '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
            }

database_config = {
            'host': 'mongodb://localhost:27017/',
            'database': 'fin-mg-database',
            'user_collection': 'users',
            'index_collection': 'indices',
            'currency_collection': 'currency',
            'equity_collection': 'equities',
            'equity_performance_collection': 'equities_performance',
            'equity_reference_collection': 'equities_reference',
            'equity_rates_collection': 'equities_rates',
            'equity_statistics_collection': 'equities_statistics',
            'currency_rates_collection': 'currency_rates',
            'country_codes_collection': 'country_codes'
            }

reference_data_config = {
            'indices_filename': 'index_data.txt',
            'currencies_filename': 'index_currency.txt',
            'target_currency': 'USD',
            'performance_for_last_n_days': 365,
            'country_codes_filename': 'country_codes.txt'
            }