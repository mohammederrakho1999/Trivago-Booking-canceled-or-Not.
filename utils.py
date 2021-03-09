import numpy as np
import pandas as pd 
from sklearn import preprocessing


def toBinary(featureCol,df):
    values = set(df[featureCol].unique())
    newCol = [ "{}_{}".format(featureCol, val) for val in values]
    for val in values:
        df["{}_{}".format(featureCol, val)] = df[featureCol].map(lambda x: 1 if x == val else 0)
    return  newCol 

def NomalizeTheData(df):
    x = df.values.reshape(-1, 1)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)