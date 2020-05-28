import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from use import *

def predict(ticker,no_of_days):

    df=stock(ticker)

    a=df.loc[0]['open']
    b=df.loc[0]['high']
    c=df.loc[0]['low']

    df.drop('volume',axis=1,inplace=True)

    #date=input("yyyy-mm-dd:")

    #h=df[df['timestamp']==date]['high'].tolist()

    #l=df[df['timestamp']==date]['low'].tolist()

    #predict_matter=[o[0],h[0],l[0]]


    df['label']=df['close']

    df['label']=df['label'].shift(no_of_days)

    X=np.array(df[['open','high','low']])

    X_predict=X[:no_of_days]

    X=X[no_of_days:]

    y = np.array(df['label'])

    y=y[no_of_days:]

    X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.3,random_state=101)

    lm=LinearRegression()

    lm.fit(X_train,y_train)

    predictions=lm.predict(X_test)

    #confidence = lm.score(X_test,y_test)

    #print('Confidence:',confidence)
    predictions_2=[]
    predictions_1=lm.predict(X_predict)
    k=predictions_1.tolist()
    for i in k:
        predictions_2.append(round(i,3))
    predictions_1=round(predictions_1.tolist()[0],3)
    print("Predictions: ",predictions_1)

    return a,b,c,predictions_1,predictions_2
