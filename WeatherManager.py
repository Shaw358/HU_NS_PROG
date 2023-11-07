import math

import requests
from datetime import datetime, timedelta


def GetWeatherFromTomorrow(cityName):
    api_key = '637539cc81affb2758a3a4f6278f3f12'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    location = cityName + ',NL'

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_date = int(tomorrow.timestamp())

    # Make the API request to get the weather forecast
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract temperature information for tomorrow
        weather_forecast = data['list']
        for forecast in weather_forecast:
            forecast_date = forecast['dt']
            if forecast_date >= tomorrow_date:
                temperature_kelvin = forecast['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
                roundedNumber = round(temperature_celsius)
                strConversion = str(roundedNumber)
                return strConversion
    else:
        print('Failed to retrieve the forecast. Status code:', response.status_code)
