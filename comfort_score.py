def comfort_score(temp, humidity, wind_speed, uv=0):
    """
    Returns a score from 0-100.
    Higher = more comfortable to be outside.
    """
    score = 100

    # Temperature penalty (ideal: 20-28°C)
    if temp < 15:
        score -= (15 - temp) * 3
    elif temp > 35:
        score -= (temp - 35) * 4
    elif 20 <= temp <= 28:
        score += 10  # bonus for ideal range

    # Humidity penalty (ideal: 40-60%)
    if humidity > 70:
        score -= (humidity - 70) * 0.5
    elif humidity < 30:
        score -= (30 - humidity) * 0.3

    # Wind penalty (ideal: < 20 km/h)
    if wind_speed > 20:
        score -= (wind_speed - 20) * 1.5

    # UV penalty
    if uv > 6:
        score -= (uv - 6) * 5

    return max(0, min(100, round(score)))

def best_windows(hourly_data):
    """Find the top 3 most comfortable consecutive hours."""
    scored = [(h["time"], comfort_score(
        h["temp"], h["humidity"], h["wind_speed"], h["uv"]
    )) for h in hourly_data]

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:3]
