import pandas as pd 
import numpy as np 

def calc_returns(data):
    returns = data.diff()
    return returns

def calc_log_returns(data):
    log_vals = np.log(data)
    log_rt = calc_returns(log_vals)
    return log_rt

def calc_weekly(data,type):
    if type == 'avg':
        df = data.resample('W').mean()
    if type == 'last':
        df = data.resample('W').last()
    return df

def calc_monthly(data,type):
    if type == 'avg':
        df = data.resample('BM').mean()
    if type == 'last':
        df = data.resample('M').last()
    return df

def calc_volatility(data,type):
    if type == 'month':
        df = data.resample('M').std(ddof=0)
    if type == 'week':
        df = data.resample('W').std(ddof=0)
    return df