#!/bin/bash
API_KEY=$OPENWEATHER_API_KEY
CITY="Savar,bd"

weather=$(curl -s "https://api.openweathermap.org/data/2.5/weather?q=$CITY&units=metric&appid=$API_KEY")

if [ $? -eq 0 ] && [ "$weather" != "" ]; then
    temp=$(echo $weather | jq '.main.temp | round')
    code=$(echo $weather | jq -r '.weather[0].icon')
    id=$(echo $weather | jq -r '.weather[0].id')

    # Catppuccin Colors
    yellow="#f9e2af"
    blue="#89b4fa"
    white="#cdd6f4"
    gray="#6c7086"
    red="#f38ba8"
    peach="#fab387"
    mauve="#cba6f7"
    teal="#94e2d5"

    # Weather Logic by Group ID & Icon Code
    if [[ $id -ge 200 && $id -le 232 ]]; then
        icon="󰙾"; color="$red"      # Thunderstorm
    elif [[ $id -ge 300 && $id -le 321 ]]; then
        icon="󰖎"; color="$teal"     # Drizzle
    elif [[ $id -ge 500 && $id -le 531 ]]; then
        icon="󰖗"; color="$blue"     # Rain
    elif [[ $id -ge 600 && $id -le 622 ]]; then
        icon="󰼶"; color="$white"    # Snow
    elif [[ $id -eq 781 ]]; then
        icon="󰼸"; color="$red"      # Tornado
    elif [[ $id -ge 701 && $id -le 771 ]]; then
        icon="󰖑"; color="$gray"     # Mist, Smoke, Haze, Dust, Fog, Sand
    elif [[ $id -eq 800 ]]; then
        if [[ "$code" == *"d"* ]]; then
            icon="󰖙"; color="$yellow" # Clear Day
        else
            icon="󰖔"; color="$mauve"  # Clear Night
        fi
    elif [[ $id -eq 801 ]]; then
        if [[ "$code" == *"d"* ]]; then
            icon="󰖕"; color="$peach"  # Few Clouds Day
        else
            icon="󰼱"; color="$gray"   # Few Clouds Night
        fi
    elif [[ $id -ge 802 && $id -le 804 ]]; then
        icon="󰖐"; color="$gray"     # Scattered/Broken/Overcast Clouds
    else
        icon=""; color="$yellow"   # Default fallback
    fi

    echo "<span color='$color'>$icon</span> <span color='#cdd6f4'>$temp°C</span>"
else
    echo "<span color='#f38ba8'>󰖪</span>"
fi