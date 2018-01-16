import requests
from lxml import html
import json


def xpath_print():
    
    
    headers = {'content-type': 'application'}

    page = requests.get('http://www.dragonballz.com', auth=('username', 'password'), headers=headers)

    tree = html.fromstring(page.content)

    currency = tree.xpath('//*[@id="main-links"]/div[1]/ul/li[1]/div/a')


    print (currency)

xpath_print()

