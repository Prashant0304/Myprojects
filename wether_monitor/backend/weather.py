import requests
import time
from datetime import datetime
from config import API_KEY, CITY_IDS, UPDATE_INTERVAL
from database import create_table

def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/group?id={','.join(CITY_IDS)}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def process_weather_data(weather_data):
    summaries = {}
    for city in weather_data['list']:
        city_name = city['name']
        temp = city['main']['temp']
        feels_like = city['main']['feels_like']
        condition = city['weather'][0]['main']
        timestamp = datetime.fromtimestamp(city['dt']).date()
        
        if timestamp not in summaries:
            summaries[timestamp] = {'temps': [], 'conditions': []}
        
        summaries[timestamp]['temps'].append(temp)
        summaries[timestamp]['conditions'].append(condition)
    
    return summaries

def calculate_daily_summary(summaries):
    for date, data in summaries.items():
        avg_temp = sum(data['temps']) / len(data['temps'])
        max_temp = max(data['temps'])
        min_temp = min(data['temps'])
        dominant_condition = max(set(data['conditions']), key=data['conditions'].count)
        
        # Store summary in the database
        store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)

def store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = connect_db()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO daily_weather (date, avg_temp, max_temp, min_temp, dominant_condition)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (date) DO UPDATE SET
                    avg_temp = EXCLUDED.avg_temp,
                    max_temp = EXCLUDED.max_temp,
                    min_temp = EXCLUDED.min_temp,
                    dominant_condition = EXCLUDED.dominant_condition;
            """, (date, avg_temp, max_temp, min_temp, dominant_condition))

def main():
    create_table()
    while True:
        weather_data = fetch_weather_data()
        summaries = process_weather_data(weather_data)
        calculate_daily_summary(summaries)
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
