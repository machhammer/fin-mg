
import pandas as pd

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import Tokenizer

from datetime import datetime, date, timedelta

import time
import pickle


def get_file():
    now = datetime.today().now()

    now = date(2019, 11, 20)

    path = "/Users/machhammer/" 
    file_name = "tweets_" + str(now.day) + "_" + str(now.month) + "_" + str(now.year) + ".txt"

    print(path + file_name)

    df = pd.read_csv(path + file_name, sep=';', header=None, names=['text', 'user', 'location', 'followers', 'created_at', 'category'])
    text = df['text'].values

    json_file = open(path + 'model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights(path + 'weights.best.hdf5')
    print("Loaded model from disk")

    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    score = loaded_model.predict(X, Y, verbose=0)
    
    return text



if __name__ == '__main__':
    print("Twitter started")
    get_file()