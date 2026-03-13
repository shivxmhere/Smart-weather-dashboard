# 🌤️ Smart Weather Dashboard

Day 1/35 of my #35DaysOfProjects challenge.

A Python terminal dashboard that fetches live weather and calculates a 
**Comfort Score** to recommend the best hours to go outside or study.

## Features
- Live weather via OpenWeatherMap API
- Comfort Score algorithm (temp + humidity + wind)
- Best 3-hour window recommendations
- Daily CSV logging

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install requests rich python-dotenv
   ```
3. Add your OpenWeatherMap API key to a `.env` file:
   ```
   OPENWEATHER_API_KEY=your_key_here
   ```
4. Run the dashboard:
   ```bash
   python main.py
   ```

## Tech Stack
Python · requests · rich · OpenWeatherMap API
