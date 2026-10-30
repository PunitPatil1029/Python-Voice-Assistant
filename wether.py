
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

print("API key loaded:", bool(API_KEY))
print("API key length:", len(API_KEY) if API_KEY else 0)

def get_weather(city):

    if not API_KEY:
        return "Weather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            return (
                f"The weather in {city} is {description}. "
                f"Temperature is {temperature} degrees Celsius. "
                f"Humidity is {humidity} percent."
            )


        elif response.status_code == 401:

            return "Weather API error: " + data.get("message", "Invalid API key")

        elif response.status_code == 404:
            return "City not found. Please try another city."

        else:
            return "Unable to get weather information."

    except requests.exceptions.RequestException:
        return "Please check your internet connection."


# Test weather feature
if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
