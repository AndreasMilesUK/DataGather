# crtl + /
import pandas as pd
from pandas import * #I suspect formating it like this will make all pandas modules available
import requests
from bs4 import BeautifulSoup
import csv


companies = 'C:\Companies.xlsx'
companies = pd.read_excel(companies,
                         sheet_name='Global',           
                          header=0,
                          index_col= 3,
                          names=None,
                          converters=None,
                          dtype=None,
                          keep_default_na=True)

comp_list = companies["Exchange:Ticker"].tolist()
tickers = []

for ticker in comp_list:
    try:      
        code = ticker.split(':')[1]
        tickers.append(code)
    except:
        pass

#comp_list = []
#for name in comp:
#    l = name.rfind('(')
#    comp_list.append(name[:l-1])


names = []
for list in tickers:
    url = 'https://www.reuters.com/finance/stocks/company-officers/'+list
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    #listc = str.lower(list.split(' ', 1)[0])
    for link in soup.find_all('a'):
        title = link.text
        if searchword in title and 'linkedin' in title:
            names.append(title,link)

with open('Names.txt','w') as f:
    f.write(','.join(names))

