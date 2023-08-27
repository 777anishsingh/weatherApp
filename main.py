import json
import os

import requests

try:
    city = input("Enter the name of city: ")
    url = f"htt ps://api.weatherapi.com/v1/current.json?key=705e6ed262264ce8bd6173335232408&q={city}"

    r = requests.get(url)
    # print(r.text)
    wdic = json.loads(r.text)
    temp = wdic["current"]["temp_c"]
    print(f"Current weather in {city} is - ", temp, "°C")

    # to convert from text to speech
    command = f' echo Current weather in {city} is - {temp} °Celsius | powershell -command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"'
    os.system(command)

# exception handling
except Exception as errror:
    print("Error occured at ", errror)
