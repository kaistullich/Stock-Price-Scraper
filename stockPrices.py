from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
	userStockInput = input("Please enter stock ticker: ")
	# Puts input into all CAPS
	userStockInputCap = userStockInput.upper()

	# specify the url
	url = ('https://finance.yahoo.com/quote/{}?ltr=1').format(userStockInputCap)

	# query the website and return the html to the variable 'page'
	page = urlopen(url)

	# parse the html using beautiful soap and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')

	# Finding the ticker by class tag
	ticker = soup.find(class_='D(ib) Maw(65%) Maw(70%)--tab768 Ov(h)').text

	print('Current information for {}:'.format(userStockInputCap), ticker)

except Exception as e:
	print ('The following error has occured:', str(e))