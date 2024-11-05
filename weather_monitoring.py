import requests
import schedule
import time
import pandas as pd

API_KEY = '531f05a1a98ac1baff9cb43aa76a1bae'  
CITY = 'Delhi'
weather_data = []

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_celsius = data['main']['temp'] - 273.15
        condition = data['weather'][0]['main']
        timestamp = pd.to_datetime(data['dt'], unit='s')

        entry = {'City': city, 'Temp': temp_celsius, 'Condition': condition, 'Timestamp': timestamp}
        weather_data.append(entry)
        print(f"Logged: {entry}")
    else:
        print(f"Error {response.status_code}: Unable to fetch weather data.")

schedule.every(5).minutes.do(lambda: fetch_weather_data(CITY))

print("Starting weather monitoring...")

while True:
    schedule.run_pending()
    time.sleep(1)

