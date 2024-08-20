import requests
import re

class WeatherService:
    API_KEY = 'da8c497f530bea97455b28482b9df8db'
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    def weather_info(self, reply):
        city_match = re.search(r"\b(\w+)\s+hava durumu\b", reply)
        if city_match:
            city_name = city_match.group(1)
            return self.get_weather(city_name)
        else:
            city_name = input("Hangi şehrin hava durumu bilgisini almak istersiniz? ")
            return self.get_weather(city_name)

    def get_weather(self, city_name):
        complete_url = f"{self.BASE_URL}q={city_name}&appid={self.API_KEY}&units=metric&lang=tr"
        response = requests.get(complete_url)

        try:
            data = response.json()
        except ValueError:
            return "Hava durumu bilgisi alınamadı, lütfen daha sonra tekrar deneyin."

        if data["cod"] != "404":
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"{city_name} için hava durumu: Hava {temperature} derece ve {weather_desc}."
        else:
            return "Şehir bulunamadı, lütfen geçerli bir şehir adı girin."




