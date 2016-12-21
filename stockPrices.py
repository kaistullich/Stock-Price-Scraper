from bs4 import BeautifulSoup
from urllib.request import urlopen

# specify the url
url = 'https://www.google.com/finance?cid=22144'

# query the website and return the html to the variable 'page'
page = urlopen(url)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Finding AAPL id tag and only showing the text inside of the tag
aapl = soup.find(id='ref_22144_l').text

print('Current AAPL share price is:', aapl)