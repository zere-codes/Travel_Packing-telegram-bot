import requests
import os

def get_weather(city):
    try:
        api_key = os.getenv("WEATHER_KEY")

        link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(link)
        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]

        weather_map = {
            "Rain": "Дождь🌧️",
            "Clear": "Солнечно☀️",
            "Snow": "Снег❄️",
            "Clouds": "Облачно☁️",
            "Drizzle": "Морось",
            "Thunderstorm": "Гроза⚡",
            "Mist": "Туман🌫️"
        }

        weather_russki = weather_map.get(weather, weather)

        return temp, weather_russki

    except Exception:
        return None, None