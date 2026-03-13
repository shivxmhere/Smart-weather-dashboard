import csv
import os
from datetime import datetime

def log_weather(hourly, city):
    filename = f"weather_log_{city}.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["fetched_at", "time", "city", "temp", "humidity", "wind_speed"])
        if not file_exists:
            writer.writeheader()
        for h in hourly:
            writer.writerow({
                "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "time": h["time"],
                "city": city,
                "temp": h["temp"],
                "humidity": h["humidity"],
                "wind_speed": h["wind_speed"]
            })
    print(f"\nDONE: Weather logged to {filename}")
