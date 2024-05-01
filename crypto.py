from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

stock_data = soup.findAll("td")


counter = 0
for x in range(5):
    symbol = stock_data[counter].text.split('-')[0].strip()
    name = stock_data[counter+1].text.split(' ')[0].strip()
    current_price = stock_data[counter+2].text
    percent_change = stock_data[counter+4].text
    corresponding_price = stock_data[counter+3].text

    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Current Price: {current_price}")
    print(f"Percent Change (24hr): {percent_change}")
    print(f"Corresponding Price: {corresponding_price}")

    print()
    counter += 12
