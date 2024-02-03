import requests
from bs4 import BeautifulSoup

# Specify the URL of the Google Finance page for the stock you want to fetch
stock_symbol = "GOOGL"  # Google's parent company, Alphabet Inc.
url = f"https://www.google.com/finance/quote/{stock_symbol}:NASDAQ"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the element that contains the current stock price (you may need to inspect the webpage to find the correct element)
    price_element = soup.find("div", {"class": "YMlKec fxKbKc"})

    # Extract the stock price
    if price_element:
        stock_price = price_element.text
        print(f"The current stock price for {stock_symbol} is: {stock_price}")
    else:
        print(f"Could not find the stock price for {stock_symbol}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

##soup.prettify() method to turn the BeautifulSoup object into a nicely formatted string and fixes common html mistakes like adding missed closing tags