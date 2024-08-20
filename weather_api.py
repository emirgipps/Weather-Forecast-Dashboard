import requests

def get_weather(city):
    api_key = "4d2f83890bbbfac0a4e3d39f7bac28ac"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
