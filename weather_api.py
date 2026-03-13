import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city="Delhi"):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "cnt": 8  # next 24 hours in 3-hour intervals
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        hourly = []
        for item in data["list"]:
            hourly.append({
                "time": item["dt_txt"],
                "temp": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "wind_speed": item["wind"]["speed"],
                "description": item["weather"][0]["description"],
                "uv": 0
            })
        return hourly, data["city"]["name"]
    except Exception as e:
        # Fallback to mock data for demonstration if API fails (e.g., 401 Unauthorized)
        mock_file = os.path.join(os.path.dirname(__file__), "mock_weather.json")
        if os.path.exists(mock_file):
            with open(mock_file, "r") as f:
                hourly = json.load(f)
            return hourly, f"{city} (Demo Mode)"
        raise e
