import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from use import *

def timestamp(ticker,date):
    try:
        df=stock(ticker)
        o=df[df['timestamp']==date]['open'].tolist()
        h=df[df['timestamp']==date]['high'].tolist()
        l=df[df['timestamp']==date]['low'].tolist()
        c=df[df['timestamp']==date]['close'].tolist()
        return o[0],h[0],l[0],c[0]
    except:
        o='Error'
        h='Error'
        l='Error'
        c='Error'
        return o,h,l,c
