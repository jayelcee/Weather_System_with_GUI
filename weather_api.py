import requests
import sqlite3
from datetime import datetime

API_KEY = "7ca96439d4b14c7fbb761544230711"


class WeatherApi:
    def __init__(self):
        self.db_path = 'weather_data_demo.db'

    def db_connect(self):
        return sqlite3.connect(self.db_path)

    def request_forecast(self, location="Philippines"):
        url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&alerts=yes&days=7"
        response = requests.request("GET", url, timeout=300)
        json = response.json()

        # Store the fetched data into the database
        self.store_forecast_data(json)

        return json

    def request_prev_forecast(self, location="Philippines", date=datetime.now().date()):
        date = datetime.strptime(str(date), "%Y-%m-%d").date()
        url = f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q={location}&dt={date}"
        response = requests.request("GET", url)
        json = response.json()

        # Store the fetched data into the database
        self.store_forecast_data(json)

        return json

    def store_forecast_data(self, data):
        conn = self.db_connect()
        cursor = conn.cursor()

        # Check if the location already exists and get its ID
        location = data['location']
        cursor.execute('SELECT location_id FROM locations WHERE name = ?', (location['name'],))
        location_row = cursor.fetchone()

        if location_row:
            location_id = location_row[0]
        else:
            # Insert location data and get the new ID
            cursor.execute('''
                INSERT INTO locations (name, country, region)
                VALUES (?, ?, ?)
            ''', (location['name'], location['country'], location['region']))
            location_id = cursor.lastrowid
            conn.commit()

        # Insert forecast data
        for forecast in data['forecast']['forecastday']:
            cursor.execute('''
                INSERT INTO forecasts (location_id, date, max_temp, min_temp, avg_temp, 
                                       total_precipitation, max_wind_speed)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                location_id,
                forecast['date'],
                forecast['day']['maxtemp_c'],
                forecast['day']['mintemp_c'],
                forecast['day']['avgtemp_c'],
                forecast['day']['totalprecip_mm'],
                forecast['day']['maxwind_kph'],
            ))
            forecast_id = cursor.lastrowid

            # Insert condition data
            for hour in forecast['hour']:
                cursor.execute('''
                    INSERT INTO conditions (forecast_id, time, temperature, wind_speed, precipitation, 
                                            cloud_cover, humidity, pressure, icon)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    forecast_id,
                    hour['time'],
                    hour['temp_c'],
                    hour['wind_kph'],
                    hour['precip_mm'],
                    hour['cloud'],
                    hour['humidity'],
                    hour['pressure_in'],
                    hour['condition']['icon'],
                ))

            # Insert astro data
            astro = forecast['astro']
            cursor.execute('''
                INSERT INTO astro (forecast_id, sunrise, sunset, moonrise, moonset)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                forecast_id,
                astro['sunrise'],
                astro['sunset'],
                astro['moonrise'],
                astro['moonset'],
            ))

        conn.commit()
        conn.close()