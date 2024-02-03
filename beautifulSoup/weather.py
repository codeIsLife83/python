import requests
from bs4 import BeautifulSoup


def get_weather_for_livingston_tx():
    # Specify the URL of the weather page for Livingston, TX
    url = "https://weather.com/weather/today/l/30.7062,-94.9315"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Locate the element that contains the current temperature
        temperature_element = soup.find(
            "span", {"class": "CurrentConditions--tempValue--MHmYY"}
        )

        # Locate the element that contains the current weather condition
        condition_element = soup.find(
            "div", {"class": "CurrentConditions--phraseValue--mZC_p"}
        )

        # Extract the temperature and condition
        temperature = temperature_element.text.strip()
        condition = condition_element.text.strip()

        return f"Current temperature in Livingston, TX: {temperature}, Condition: {condition}"


    else:
        return "Failed to retrieve weather information."


# # Example usage:
# weather_info = get_weather_for_livingston_tx()
# print(weather_info)


# def get_weather(city, state):
#     # Construct the URL for the weather page based on the user's input
#     url = f"https://weather.com/weather/today/l/{city},{state}"

#     # Send an HTTP GET request to the URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Locate the element that contains the current temperature
#         temperature_element = soup.find(
#             "span", {"class": "CurrentConditions--tempValue--MHmYY"}
#         )

#         # Locate the element that contains the current weather condition
#         condition_element = soup.find(
#             "div", {"class": "CurrentConditions--phraseValue--mZC_p"}
#         )
#         # Extract the temperature and condition
#         temperature = temperature_element.text.strip()
#         condition = condition_element.text.strip()

#         return f"Current temperature in {city}, {state}: {temperature}, Condition: {condition}"

#     else:
#         return "Failed to retrieve weather information."


# # Prompt the user to enter a city and state
# city = input("Enter the city: ")
# state = input("Enter the state: ")

# # Example usage:
# weather_info = get_weather(city, state)
# print(weather_info)
