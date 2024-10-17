import psycopg2
from psycopg2 import sql

def connect_db():
    conn = psycopg2.connect(
        dbname='weather_db',
        user='your_user',
        password='your_password',
        host='db',
        port='5432'
    )
    return conn

def create_table():
    conn = connect_db()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_weather (
                    date DATE PRIMARY KEY,
                    avg_temp FLOAT,
                    max_temp FLOAT,
                    min_temp FLOAT,
                    dominant_condition VARCHAR
                )
            """)

