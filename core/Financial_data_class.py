import get_NASDAQCPH_tikers as gs 
import match_cvrs as mc
import get_Financial_data as stonks
import calc_stuff as calc
import pandas as pd
import numpy as np

class financialMeasures():
    """
    A class that contains the stock price data and calculated measures for danish publicly traded companies.

    Attributes:
    Tickers: a list of tickers on the NASDAQ Copenhagen exchange
    Prices: Adjusted Close price for all tickers
    Volume: Volume for all tickers
    ....: Other measures for all tickers
    CVRs: CVR numbers for the companies.
    ###

    Methods:
    
    constructor method: Scrapes NASDAQ copenhagen for companies and gets data using yahoo finance.
    calculate measures: Calculates the measures and populates the attributes.
    get_measure: method that returns a dataframe for a company/list of companies with the selcted measure. 
    get_company: method that returns a dataframe for a measure/list of measures with selected company. 
    get_CVR: method that returns a dataframe with tickers and associated CVR numbers
    get_everything: method that returns all data avaliable in one dataframe.    
    """    
    
    def __init__(self):
        df_tickers = gs.get_tickers()
        self.tickers = df_tickers[['Symbol']].to_numpy().reshape(-1)
        self.cvrs = mc.match_cvrs()
        self.raw_download = stonks.get_stonks(self.tickers)

        self.adj_close = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='Adj Close']
        
        self.open = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='Open']

        self.volume = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='Volume']
        
        self.close = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='Close']
        
        self.high = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='High']
        
        self.low = self.raw_download.iloc[:,  self.raw_download.columns.get_level_values(0)=='Low']

        self.returns = calc.calc_returns(self.adj_close)
        self.log_returns = calc.calc_log_returns(self.adj_close)

    def to_weekly(self, data,type= 'last'):
        df = calc.calc_weekly(data,type)
        return df

    def to_monthly(self, data,type = 'last'):
        df = calc.calc_monthly(data,type)
        return df

    def volatility(self, data,type = 'week'):
        df = calc.calc_volatility(data,type)
        return df   

    def create_grand_table(self,type = 'daily'):
        if type == 'daily':
            df = self.raw_download.merge(self.returns,left_index=True, right_index=True)
            df = df.merge(self.log_returns,left_index=True, right_index=True)
            num_rows = df.shape[0]

            symbols = df.columns.get_level_values(1).unique().to_list()
            match = set(self.cvrs['Symbol'])== set(symbols)
            print('Do symbols from CVR register and NASDAQ match? '+ str(match))

            value = ['CVR']*len(symbols)
            tuples = list(zip(value,symbols))
            index = pd.MultiIndex.from_tuples(tuples, names=['Value', 'Stock'])


            array = np.full((num_rows,1), self.cvrs.loc[self.cvrs['Symbol'] == symbols[0],'CVR'].iloc[0])
            for i in range(1,len(symbols)):
                new_array = np.full((num_rows,1), self.cvrs.loc[self.cvrs['Symbol'] == symbols[i],'CVR'].iloc[0])
                array = np.append(array,new_array,axis = 1)
            df2 = pd.DataFrame(array,index=df.index,columns = index)

            df = df.merge(df2,left_index=True, right_index=True)
            
            values = df.columns.get_level_values(0).unique().to_list()
            values = list(zip(values,symbols))

            df = df.unstack().unstack(level=0).reset_index(level=0, drop=False).rename_axis('Date')
            df.to_csv('output_data/daily_data.csv')
        return df