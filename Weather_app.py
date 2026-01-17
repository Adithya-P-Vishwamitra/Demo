import requests
import json
import tkinter as tk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
    
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather():
     city = city_entry.get().capitalize()
     try:
        url = f'http://api.weatherapi.com/v1/current.json?key=<API_KEY>&q={city}'
        content = requests.get(url)
        wdic = json.loads(content.text)

        temp = wdic['current']['temp_c']
        condition = wdic['current']['condition']['text']
        wind = wdic['current']['wind_mph']
        humidity = wdic['current']['humidity']

        result = (
            f"Current temperature in {city}: {temp}°C\n"
            f"Weather condition: {condition}\n"
            f"Wind speed: {wind} mph\n"
            f"Humidity: {humidity}%"
        )

        result_label.config(text=result)

        speak(f"The current temperature in {city} is {temp} degrees Celsius. "
              f"The weather is {condition}. Wind speed is {wind} miles per hour. "
              f"Humidity is {humidity} percent.")

     except Exception as e:
         messagebox.showerror("Error", "Could not fetch weather data.\nCheck your internet or city name.")
         speak("Sorry, I could not fetch the weather for that city.")


root = tk.Tk()
root.title("Weather App with Voice")
root.geometry("370x320")

tk.Label(root, text="Enter City Name:", font=('Arial', 12)).pack(pady=10)
city_entry = tk.Entry(root, width=25, font=('Arial', 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, font=('Arial', 12), bg='lightblue').pack(pady=10)
result_label = tk.Label(root, text="", font=('Arial', 11), justify='left')
result_label.pack(pady=20)

root.mainloop()
