from http.server import BaseHTTPRequestHandler
import requests
import os
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        city = query_components.get("city", ["Delhi"])[0]
        
        api_key = os.environ.get("OPENWEATHER_API_KEY")
        base_url = "https://api.openweathermap.org/data/2.5/forecast"
        
        try:
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric",
                "cnt": 8
            }
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            hourly = []
            for item in data["list"]:
                hourly.append({
                    "time": item["dt_txt"],
                    "temp": item["main"]["temp"],
                    "humidity": item["main"]["humidity"],
                    "wind_speed": item["wind"]["speed"],
                    "description": item["weather"][0]["description"]
                })
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                "city": data["city"]["name"],
                "hourly": hourly
            }).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
