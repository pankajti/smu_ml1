import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt

request_format = """
http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&ResponseGroup=Small&SearchIndex=Music&Title=Blue&AWSAccessKeyId={}&AssociateTag={}&Timestamp={}&Signature={}
"""

access_key ='AKIAJ7UMQVK4M4E7EX2Q'

aws_account_id= 'mindcurd-21'

url = request_format.format(access_key, aws_account_id, '2019-09-15T10:12:12.000Z', 'pankaj')


print(url)

response  = requests.get(url)

print(response)