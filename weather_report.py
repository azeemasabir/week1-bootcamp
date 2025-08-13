import requests
import csv

API_KEY = "9a1ddb18b9ecc250f5d5129b753890c9"  # Replace with your actual OpenWeatherMap API key
CITIES = ["London", "New York", "Tokyo", "Karachi", "Sydney"]

def fetch_weather(city):
    """Fetch weather data for a city from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        }
    else:
        print(f"Error fetching {city}: {data.get('message', 'Unknown error')}")
        return None

def save_to_csv(data, filename="weather.csv"):
    """Save list of weather data dicts to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["city", "temperature", "weather"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def find_extremes(data):
    """Find the hottest and coldest cities."""
    hottest = max(data, key=lambda x: x["temperature"])
    coldest = min(data, key=lambda x: x["temperature"])
    return hottest, coldest

if __name__ == "__main__":
    weather_data = []
    for city in CITIES:
        info = fetch_weather(city)
        if info:
            weather_data.append(info)

    if weather_data:
        save_to_csv(weather_data)
        hottest, coldest = find_extremes(weather_data)
        print(f"Hottest city: {hottest['city']} ({hottest['temperature']}°C)")
        print(f"Coldest city: {coldest['city']} ({coldest['temperature']}°C)")
