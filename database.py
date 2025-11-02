"""
Модуль для работы с базой данных SQLite
"""
import sqlite3
from datetime import datetime
from config import Config

class WeatherDatabase:
    """Класс для работы с историей запросов погоды"""
    
    def __init__(self, db_path=None):
        self.db_path = db_path or Config.DATABASE_PATH
        self.init_db()
    
    def init_db(self):
        """Инициализация базы данных"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                country TEXT,
                temperature REAL,
                feels_like REAL,
                humidity INTEGER,
                wind_speed REAL,
                description TEXT,
                icon TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_record(self, city, country, temperature, feels_like, humidity, wind_speed, description, icon):
        """Добавление записи в историю"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO weather_history 
            (city, country, temperature, feels_like, humidity, wind_speed, description, icon)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (city, country, temperature, feels_like, humidity, wind_speed, description, icon))
        
        conn.commit()
        conn.close()
    
    def get_history(self, limit=10):
        """Получение истории запросов"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM weather_history 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_city_stats(self, city):
        """Получение статистики по городу"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT COUNT(*) as count, MAX(timestamp) as last_query
            FROM weather_history 
            WHERE LOWER(city) = LOWER(?)
        ''', (city,))
        
        result = cursor.fetchone()
        conn.close()
        
        return {'count': result[0], 'last_query': result[1]}

