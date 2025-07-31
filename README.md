# Weather Checker CLI Tool

A simple command-line tool built in Python that fetches current weather information for any city using the OpenWeatherMap API.

## Features

- Get real-time weather for any city
- Choose between Celsius or Fahrenheit
- Robust error handling with automatic retries
- Lightweight and beginner-friendly
- Learn APIs, CLI tools (`argparse`), and JSON parsing

## Demo

```bash
$ python weather_cli.py --city Delhi --unit metric

Weather in Delhi:
Condition: Rain
Temperature: 27.05 °C
Humidity: 94%

## Requirements

requests module (pip install requests)

## Setup & Usage
1. Clone the repo:
git clone https://github.com/PriyanshiSinghai/WeatherChecker_CLI.git

2. Get your free API key from OpenWeatherMap

3. Paste your API key into the script (weather_cli.py)

