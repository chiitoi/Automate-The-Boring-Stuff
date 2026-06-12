#Chapter 20 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter20.html

import requests, json, pprint, ezgmail

city = 'new york'

headers = {
    "User-Agent": "practice-app/0.0.1"
}

#convert a city to geo-coordinates
city_response = requests.get(
    "https://photon.komoot.io/api/",
    params={"q": city,
            "limit": 1},
    headers=headers,
    timeout=10
)

try:
    city_response.raise_for_status()
except Exception as exc:
    print(f'There was a problem:', exc)

city_decode = json.loads(city_response.text)
city_coordinates = city_decode['features'][0]['geometry']['coordinates']
#round to 4 decimal places because api.weather.gov only supports 4 decimal places
longitude = round(city_coordinates[0],4)
latitude = round(city_coordinates[1],4)

#query for the weather
weather_coordinates = f'https://api.weather.gov/points/{latitude},{longitude}'
coordinate_response = requests.get(weather_coordinates, headers=headers)

try:
    coordinate_response.raise_for_status()
except Exception as exc:
    print(f'There was a problem:', exc)

coordinate_decode = json.loads(coordinate_response.text)
#pprint.pprint(coordinate_decode)
"""
    'forecast': 'https://api.weather.gov/gridpoints/TBW/71,97/forecast',
    'forecastGridData': 'https://api.weather.gov/gridpoints/TBW/71,97',
    'forecastHourly': 'https://api.weather.gov/gridpoints/TBW/71,97/forecast/hourly',
    'forecastOffice': 'https://api.weather.gov/offices/TBW',
    'forecastZone': 'https://api.weather.gov/zones/forecast/FLZ151',
"""

#this returns a link to the forecast URL
forecast_URL = coordinate_decode['properties']['forecast']
forecast_response = requests.get(forecast_URL,headers=headers)

try:
    forecast_response.raise_for_status()
except Exception as exc:
    print(f'There was a problem:', exc)

forecast_decode = json.loads(forecast_response.text)
detailed_forecast = forecast_decode['properties']['periods'][0]['detailedForecast']

with open ("recipient_email.txt") as f:
    recipient_email = f.read().strip()

if 'showers' in detailed_forecast:
    ezgmail.send(recipient_email, f'Bring an umbrella! Forecast for {city}', detailed_forecast)