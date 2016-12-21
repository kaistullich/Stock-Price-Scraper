from bs4 import BeautifulSoup
from urllib.request import urlopen

userStockInput = input("Please enter stock ticker: ")

# specify the url
url = ('https://finance.yahoo.com/quote/{}?ltr=1').format(userStockInput.upper())

# query the website and return the html to the variable 'page'
page = urlopen(url)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Finding the ticker by class tag
ticker = soup.find(class_='D(ib) Maw(65%) Maw(70%)--tab768 Ov(h)').text

print('Current information for {}:'.format(userStockInput.upper()), ticker)