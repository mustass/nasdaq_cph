import get_started as gs 
import match_cvrs as mc
import get_stonks as stonks
import calc_stuff as calc

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

Finance =financialMeasures()

#print(Finance.log_returns)
print(Finance.to_monthly(Finance.returns))

    