from lxml import html
import requests

page = requests.get('https://bittrex.com/Home/Markets')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('')

#This will create a list of prices
prices = tree.xpath('')

print ('Buyers: ', buyers)
print ('Prices: ', prices)