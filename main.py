from weather_api import get_weather
from comfort_score import best_windows
from display import show_dashboard, console
from logger import log_weather

def main():
    city = input("Enter city name (default: Delhi): ").strip()
    if not city:
        city = "Delhi"
    
    console.print(f"\nFetching weather for [bold yellow]{city}[/bold yellow]...")

    try:
        hourly, city_name = get_weather(city)
        best = best_windows(hourly)

        show_dashboard(hourly, city_name, best)
        log_weather(hourly, city_name)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
