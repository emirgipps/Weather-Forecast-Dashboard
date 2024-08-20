import tkinter as tk
from weather_api import get_weather

def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data:
        weather_label.config(text=f"Temperature: {weather_data['main']['temp']}°C\n"
                                  f"Condition: {weather_data['weather'][0]['description']}")
    else:
        weather_label.config(text="City not found")

root = tk.Tk()
root.title("Weather Forecast Dashboard")

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="")
weather_label.pack(pady=10)

root.mainloop()
