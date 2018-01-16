### This is an example of how to have very clean code.
### That not only works well, but is efficient.
### Each function has 1 and only 1 job, and it does it well.

## Here are the libraries we will be using
import requests
import json

## The job of the main function is to give direction, or instructions
## To manage the battlefield, to be the quarterback.
## Main starts the program, and ends the program.
## It directs the program appropriately inbetween those states.
def Main():
	# Get the data
	data = getJsonData()
	# Print the data to stdout (console)
	# we pass the data we got from the api to this function
	# Notice the naming convention for functions
	# This is called camel case - the first letter of the first word is lowercase
	# The rest of the words begin with uppercase
	printToScreen(data)
	return
	
## This function gathers the data 
def getJsonData():
	## Start our web session to begin making requests
	s = requests.Session()
	
	## Gather the data from the web
	page = s.get('https://bittrex.com/api/v1.1/public/getmarkets')
	
	##Get the contents of the requests
	response = page.text
	
	#Deserialize the contents so that we can more easily work with the
	#json data.
	data = json.loads(response)
	
	#return the data
	return data
	
# This function will print Json data to the console
def printToScreen(data):
	# The most efficient way to iterate over objects/lists/arrays
	# is a for loop. There are a couple approaches - by using range, and length
    # Or by taking advantage of pythons powerful for loop
    # as you can see below element becomes an object - not just a number
    # but it could be used as a number as well.
    # Below are two different ways of getting the data.
    for i in range(len(data)):
        print (data['result'][i]['MarketCurrency'])

    ## This way is much more efficient    
    for element in data['result']:
        print (element['MarketCurrency'])

    
	
if __name__ == "__main__":
	Main()