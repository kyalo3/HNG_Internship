from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Replace with an actual API key from a weather service provider (e.g., OpenWeatherMap)
WEATHER_API_KEY = '7d5248320f6eea1f5bbc57d3a27dc8ae'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        return data["main"]["temp"]
    else:
        return None

@app.get("/api/hello")
async def hello(request: Request, visitor_name: str):
    client_ip = request.client.host
    location = "New York"  # For simplicity, assuming location is New York
    temperature = get_weather(location)
    if temperature is None:
        temperature = "unknown"

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }

    return response
