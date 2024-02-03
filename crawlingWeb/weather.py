import re
import urllib.request
import html

# https://www.weather-forecast.com/locations/Houston/forecasts/latest

listofcities = ["Houston", "Austin", "Dallas", "Dublin", "London", "New-York", "Los-Angeles", "Chicago"]

def get_weather(city):
    url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
    htmltext = urllib.request.urlopen(url).read()
    htmltext = htmltext.decode("utf-8")
    m = re.search('<span class="phrase">', htmltext)
    section = htmltext[m.end() : m.end() + 300]
    m = re.search("</span>", section)
    section = section[: m.start()]
    return html.unescape(section)

search = input("would you like to search a city? (yes/no)")
if search == "yes":
    city = input("what city would you like to search?")
    capitalized_string = city.title()
    modified_city = capitalized_string.replace(" ", "-")
    print(get_weather(modified_city))
else:
    print("ok, here are the weather forcast for some cities:")
    for city in listofcities:
        friendlyCity = city.replace("-", " ")
        print(friendlyCity + ": " + get_weather(city))

    # print(get_weather("Houston"))
    # print(get_weather("Dallas"))
    # print(get_weather("Austin"))
