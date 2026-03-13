from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from comfort_score import comfort_score

console = Console()

def score_color(score):
    if score >= 75: return "green"
    elif score >= 50: return "yellow"
    else: return "red"

def show_dashboard(hourly, city, best):
    console.print(Panel(f"[bold cyan]🌤️  Smart Weather Dashboard — {city}[/bold cyan]", 
                        box=box.DOUBLE))

    table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    table.add_column("Time", style="dim", width=20)
    table.add_column("Temp (°C)", justify="center")
    table.add_column("Humidity %", justify="center")
    table.add_column("Wind km/h", justify="center")
    table.add_column("Comfort Score", justify="center")
    table.add_column("Condition")

    for h in hourly:
        score = comfort_score(h["temp"], h["humidity"], h["wind_speed"])
        color = score_color(score)
        table.add_row(
            h["time"],
            f"{h['temp']}°C",
            f"{h['humidity']}%",
            f"{h['wind_speed']}",
            f"[{color}]{score}/100[/{color}]",
            h["description"].title()
        )

    console.print(table)

    console.print("\n[bold green]🏆 Best 3 Windows to Go Outside / Study:[/bold green]")
    for i, (time, score) in enumerate(best, 1):
        console.print(f"  {i}. [cyan]{time}[/cyan] → Comfort Score: [{score_color(score)}]{score}/100[/{score_color(score)}]")
