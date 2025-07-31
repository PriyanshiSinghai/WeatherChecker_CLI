import requests
import argparse
import sys
import time

API_KEY = "5381ec7dbb2d0c960f88e48b8c25a273"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#city = input("Enter the city name: ")

parser = argparse.ArgumentParser(description="Get a current weather for a city")
parser.add_argument("--city", required=True,help="City name to get weather for")
parser.add_argument("--unit", choices=["metric", "imperial"], default="metric", help="Unit: metric (C) or imperial (F)")
args = parser.parse_args()

city = args.city
unit = args.unit

params = {
    "q": city,
    "appid": API_KEY,
    "units": unit
}

unit_symbol = "°C" if unit == "metric" else "°F"

MAX_RETRIES = 3

for attemp in range(1,MAX_RETRIES + 1):
    try: 
        response = requests.get(BASE_URL,params=params)
        if response.status_code == 200: #success
            data = response.json()
            condition = data["weather"][0]["main"].lower()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            
            print(f"\n Weather in {city.title()}:")
            print(f"Condition: {condition.title()}")
            print(f"Temperature: {temp} {unit_symbol}")
            print(f"Humidity: {humidity}%\n")
            break
        else:
            print("\n Failed to retrieve data.")
            print("Reason:", response.json().get("message", "Unknown error"))
            if attemp < MAX_RETRIES:
                print("Retrying...\n")
                time.sleep(5)
            else:
                sys.exit("Failed after 3 attempts.")
    except requests.exceptions.RequestException as e:
        if attemp < MAX_RETRIES:
            print("Retrying...\n")
            time.sleep(5)
        else:
            sys.exit("Network errors") 