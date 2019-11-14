import requests
import itertools
import pandas as pd
import os
from bs4 import BeautifulSoup
from io import BytesIO
from zipfile import ZipFile
month_names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep' , 'oct' , 'nov','dec']
years = [f"{i:02d}"  for i in range(8, 20)]
url_sufs = [''.join(suf)  for suf in itertools.product(month_names , years)]
url_root = 'https://www.nseindia.com/content/indices/mcwb_{}.zip'
data_root = '/Users/pankaj/dev/data/nifty50'

for u in url_sufs :

    data_path = os.path.join(data_root, u)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    url= url_root.format(u)
    try:
        content = requests.get(url)
        zf = ZipFile(BytesIO(content.content))
        for item in zf.namelist():
            zf.extract(item, path=data_path)
        print("done for {} ".format(url))
    except:
        print("error for {} ".format(url))


