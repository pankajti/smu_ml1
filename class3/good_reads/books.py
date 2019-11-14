
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt
import json

#https://www.goodreads.com/user/82493102/following.xml?key=fok6JIObxiZTZQZ8IJgFUg

key = 'fok6JIObxiZTZQZ8IJgFUg'
secret =  'QXlESrrOJ2kJSbdsAt0N2frzBlpd0RM59II2M2lxnc'

with open(r'/Users/pankaj/Downloads/ol_cdump_2019-08-31.txt') as f:
    #content = f.readlines()
    for c in f:
        j= json.loads(c.split('\t')[-1])
        print()
# you may also want to remove whitespace characters like `\n` at the end of each line
