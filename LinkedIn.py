# crtl + /
import pandas as pd
from pandas import * #I suspect formating it like this will make all pandas modules available
import requests
from bs4 import BeautifulSoup
import csv


companies = 'C:\Companies.xlsx'
companies = pd.read_excel(companies,
                         sheet_name='Global',           #2nd sheet of the workbook
                          header=0,
                          index_col= 2,
                          names=None,
                          converters=None,
                          dtype=None,
                          keep_default_na=True)

comp_list = companies["Company Name"].tolist()
print(comp_list)


names = []
for list in comp_list:
    url = 'https://www.google.com/search?q=' + list + ' LinkedIn' + ' HR Manager UK'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    listc = str.lower(list.split(' ', 1)[0])
    for link in soup.find_all('a'):
        title = link.text
        if listc.title() in title or listc in title :
            names.append(title)

with open('Names.txt','w') as f:
    f.write(','.join(names))

