import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
        
    try:
        # Make API request
        url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            'key': 'YOUR_WEATHEAPI_KEY',
            'q': city
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'error' not in data:
            # Get weather data
            location = data['location']['name'] + ", " + data['location']['country']
            temp = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            wind = data['current']['wind_kph']
            
            # Update labels
            weather_info.config(
                text=f"Location: {location}\n"
                     f"Temperature: {temp}°C\n"
                     f"Condition: {condition}\n"
                     f"Humidity: {humidity}%\n"
                     f"Wind: {wind} km/h"
            )
        else:
            messagebox.showerror("Error", data['error']['message'])
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

# Create widgets
tk.Label(root, text="Enter City:").pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_info = tk.Label(root, text="", justify='left')
weather_info.pack(pady=20)

# Start the app
root.mainloop()