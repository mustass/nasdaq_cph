import get_NASDAQCPH_tikers as tk
import pandas as pd 
import numpy as np
from fuzzywuzzy import process

def match_cvrs():
    tickers = tk.get_tickers()
    data_file = 'Virk_CVRS/CVR.xlsx'

    CVR = pd.read_excel(data_file,
    sheet_name=0,
    header=0,
    index_col=False,
    keep_default_na=True,
    encoding='utf-8'
    )
    CVR['Navn'] = CVR['Navn'].astype("string")
    CVRs_list = list()
    for company in range(len(tickers['Name'])):
        ToMatch = str(tickers.iloc[company]['Name'])
        strOptions = CVR['Navn']
        #Ratios = process.extract(ToMatch,strOptions)
        match = process.extractOne(ToMatch,strOptions)
        cvrnr = CVR['CVR-nummer'][CVR['Navn']==str(match[0])].values.item()
        
        #print(str(tickers.iloc[company]['Name'])+ str(' has CVR : ')+ str(cvrnr))
        CVRs_list.append(cvrnr)
    tickers['CVR']= np.asarray(CVRs_list)
    tickers = tickers.drop(['Fact Sheet'],axis = 1)
    #print(tickers.head())
    tickers.to_csv('output_data/tickers_w_cvr.csv')
    return tickers
