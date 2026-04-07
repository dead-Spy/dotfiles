#!/usr/bin/env python3
import requests
import json

def get_weather():
    try:
        res = requests.get("https://wttr.in/?format=j1").json()
        current = res['current_condition'][0]
        temp = current['temp_C']
        code = current['weatherCode']
        
        icons = {
            "113": "☀️", "116": "⛅", "119": "☁️", "122": "☁️",
            "143": "🌫️", "176": "🌦️", "182": "🌨️", "200": "⛈️",
            "263": "🌧️", "266": "🌧️", "293": "🌧️", "296": "🌧️",
            "302": "🌧️", "311": "🌧️", "353": "🌧️", "356": "🌧️",
        }
        icon = icons.get(code, "🌡️")
        
        return json.dumps({
            "text": f"{icon} {temp}°C",
            "tooltip": f"{current['weatherDesc'][0]['value']}\nFeels like: {current['FeelsLikeC']}°C"
        })
    except:
        return json.dumps({"text": "󰖪 Off", "tooltip": "Weather unavailable"})

print(get_weather())

