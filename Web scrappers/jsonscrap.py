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
    sort(Data)
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
    #This function sorts the json data from the bittrex website and sorts each coin title entry into its own list, 
    #It then wraps the entry in html ready for copy and paste into html file,
    #There are two functions that create 2 texts files each named after the appropriate coin name ready for use in html.
def sort(Data):
    #Lists to store coin names
    btc = []
    eth = []
    #Sorts "marketcurrency" into its desinated list
    for i in range(len(Data['result'])):
        if Data['result'][i]['BaseCurrency'] == ("BTC"):
            btc.append(Data['result'][i]['MarketCurrency'])
        if Data['result'][i]['BaseCurrency'] == ("ETH"):
            eth.append(Data['result'][i]['MarketCurrency'])
    #For loop to iterate through list and open and append to text file with the text wrapped around list entry.
    for element in btc:
        btc2 ='<option value="'+element+'">'+element+'</option>'
        print(btc2)
        with open("BTCcoins.txt", "a") as output:
            output.write('\n')
            output.write(str(btc2))
            output.close()
    for element in eth:
        eth2 ='<option value="'+element+'">'+element+'</option>'
        print(eth2)
        with open("ETHcoins.txt", "a") as output:
            output.write('\n')
            output.write(str(eth2))
            output.close()
    return


if __name__ == "__main__":
	Main()

