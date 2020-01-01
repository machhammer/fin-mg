
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
            'index_collection': 'indices'
            }

reference_data_config = {
            'indices_filename': 'index_data.txt',
            
            }