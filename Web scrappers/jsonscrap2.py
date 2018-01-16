"""
jsonscrap.py


Created by James Weeks on 11/05/17.

Copyright (c) 2017 James Weeks. 

This script works with Python 3.x

NOTE: These are learning notes.
"""







import json
import requests

def Main():
    
    Data = json_data()

    printToScreen(Data)

    return 



def json_data():
#start session python requests
    S = requests.Session()
#save page data to page variable
    Page = S.get ('https://bittrex.com/api/v1.1/public/getmarkets')
#Response will be json
    Response = Page.text

#deserialized data ready for indexing
    Data = json.loads(Response)

    #returns data
    return Data


def printToScreen(Data):
    
    for i in range(len(Data)):
        print(Data['result'][i]['MarketCurrencyLong'])


    for element in Data['result']:
        print(element['MarketCurrencyLong'])
        



if __name__ == "__main__":
	Main()



''''

Noob Code 


i = 0
while i < 260:
        i = i + 1
        ParsedValue = Data['result'][i]['MarketCurrencyLong']
        print (ParsedValue)   


for i in  range(0,263):
    ParsedValue = Data['result'][i]['MarketCurrencyLong']
    print(ParsedValue)
'''
