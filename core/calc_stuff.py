import pandas as pd 
import numpy as np 

def calc_returns(data):
    returns = data.diff()
    name = returns.columns.get_level_values(0)[0]
    new_name = name + '_returns'
    returns = returns.rename(columns={name: new_name})
    return returns

def calc_log_returns(data):
    log_rt = np.log(data)
    log_rt = log_rt.diff()
    name = log_rt.columns.get_level_values(0)[0]
    new_name = name + '_log_returns'
    log_rt = log_rt.rename(columns={name: new_name})
    return log_rt

def calc_weekly(data,type):
    if type == 'avg':
        df = data.resample('W').mean()
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_weekly_mean'
        df = df.rename(columns={name: new_name})
    if type == 'last':
        df = data.resample('W').last()
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_weekly_last'
        df = df.rename(columns={name: new_name})
    return df

def calc_monthly(data,type):
    if type == 'avg':
        df = data.resample('BM').mean()
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_monthly_avg'
        df = df.rename(columns={name: new_name})
    if type == 'last':
        df = data.resample('M').last()
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_monthly_last'
        df = df.rename(columns={name: new_name})
    return df

def calc_volatility(data,type):
    if type == 'month':
        df = data.resample('M').std(ddof=0)
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_monthly_volatility'
        df = df.rename(columns={name: new_name})
    if type == 'week':
        df = data.resample('W').std(ddof=0)
        name = df.columns.get_level_values(0)[0]
        new_name = name + '_weekly_volatility'
        df = df.rename(columns={name: new_name})
    return df