import requests
import json
import pandas as pd
def stock(ticker):
    key = 'AUFSF50DIXVQWX6X'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey='+key+'&datatype=csv'
    df = pd.read_csv(url)         #for csv read
    return df
