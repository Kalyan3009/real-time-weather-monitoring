import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY", "1c621b0f5a4d7e02cacf418143a2a291")
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(CURRENT_WEATHER_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "main": data["weather"][0]["main"],
        }
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code} - {response.text}")

def get_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)

    if response.status_code == 200:
        forecasts = response.json()["list"]
        forecast_data = []
        for forecast in forecasts:
            forecast_data.append({
                "date": forecast["dt_txt"].split(" ")[0],
                "min_temp": forecast["main"]["temp_min"],
                "max_temp": forecast["main"]["temp_max"],
                "humidity": forecast["main"]["humidity"],
                "weather_condition": forecast["weather"][0]["main"]
            })
        return forecast_data
    else:
        raise Exception(f"Failed to retrieve forecast data: {response.status_code} - {response.text}")