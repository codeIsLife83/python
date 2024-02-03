import re
import urllib.request


def make_string_float(input_str):
    while True:
        try:
            float_value = float(input_str)
            return float_value
        except ValueError:
            if not input_str:
                return None  # Cannot convert to a float, and the string is empty
            input_str = input_str[:-1]  # Remove the last character


def get_stock_price(stock_code, platform):
    url = (
        "https://www.google.com/finance/quote/" + stock_code + ":" + platform + "?hl=en"
    )
    htmltext = urllib.request.urlopen(url).read()
    htmltext = htmltext.decode("utf-8")
    m = re.search('<div class="YMlKec fxKbKc">', htmltext)
    section = htmltext[m.end() + 1 : m.end() + 10]
    result = make_string_float(section)
    if result is None:
        return "Cannot find the stock price"
    else:
        return result


stockarray = {"GOOG": "NASDAQ", "AAPL": "NASDAQ", "MSFT": "NASDAQ", "AMZN": "NASDAQ", "META": "NASDAQ", "TSLA": "NASDAQ", "NFLX": "NASDAQ", "NVDA": "NASDAQ", "PYPL": "NASDAQ", "ADBE": "NASDAQ", "AMD": "NASDAQ", "INTC": "NASDAQ", "NOKIA": "HEL", "IBM": "NYSE", "ORCL": "NYSE", "CSCO": "NASDAQ", "005930": "KRX"}

for stock in stockarray:
    print(stock + " is at $" + str(get_stock_price(stock, stockarray[stock])))



# print("Google is at $" + str(get_stock_price("GOOG", 'NASDAQ')))
# print("Apple is at $" + str(get_stock_price("AAPL", 'NASDAQ')))
# print("Microsoft is at $" + str(get_stock_price("MSFT", 'NASDAQ')))
# print("Amazon is at $" + str(get_stock_price("AMZN", 'NASDAQ')))
# print("Facebook is at $" + str(get_stock_price("META", 'NASDAQ')))
# print("Tesla is at $" + str(get_stock_price("TSLA", 'NASDAQ')))
# print("Netflix is at $" + str(get_stock_price("NFLX", 'NASDAQ')))
# print("Nvidia is at $" + str(get_stock_price("NVDA", 'NASDAQ')))
# print("Paypal is at $" + str(get_stock_price("PYPL", 'NASDAQ')))
# print("Adobe is at $" + str(get_stock_price("ADBE", 'NASDAQ')))
# print("AMD is at $" + str(get_stock_price("AMD", 'NASDAQ')))
# print("Intel is at $" + str(get_stock_price("INTC", 'NASDAQ')))
# print("Nokia is at $" + str(get_stock_price("NOKIA", 'HEL')))
# print("IBM is at $" + str(get_stock_price("IBM", 'NYSE')))
# print("Oracle is at $" + str(get_stock_price("ORCL", "NYSE")))
# print("Cisco is at $" + str(get_stock_price("CSCO", 'NASDAQ')))
# print("Samsung is at $" + str(get_stock_price("005930", "KRX")))
