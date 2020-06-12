import yfinance as yf
import get_started as gs
import pandas as pd

def get_stonks(tickers):
    tickers = tickers
    tickers_list = tickers.tolist()
    tickers_clean = list()
    for i in range(len(tickers_list)):
        ticker_string = tickers_list[i]+'.CO'
        ticker_string = ticker_string.replace(' ', '-')
        tickers_clean.append(ticker_string) 


    #define the ticker symbol
    tickerSymbol = tickers_clean

    #get data on this ticker
    tickerData = yf.download(tickerSymbol)
    #print(columns)
    #tickerData.columns = ['{}-{}'.format(x[0].replace(' ', '_'), x[1]) for x in tickerData.columns]
    tickerData.columns = pd.MultiIndex.from_tuples(tickerData.columns, names=['Value','Stock'])
    #get the historical prices for this ticker
    #tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-1-25')

    #see your data
    #print("Head the table:")
    #print(tickerData.head())
    #print("Saving to data.csv")
    tickerData.to_csv('data.csv')
    return tickerData



#tick = gs.get_tickers()
#tickers =  tick[['Symbol']].to_numpy().reshape(-1)
#lol = get_stonks(tickers)