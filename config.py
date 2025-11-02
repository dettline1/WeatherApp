"""
Конфигурация приложения Weather App
"""
import os

class Config:
    """Базовая конфигурация"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # OpenWeatherMap API
    OPENWEATHER_API_KEY = '37bb73d6f13ebefd2f32ef40c019a04b'
    OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    # База данных
    DATABASE_PATH = 'weather_history.db'
    
    # Языки
    SUPPORTED_LANGUAGES = ['ru', 'en']
    DEFAULT_LANGUAGE = 'ru'
    
    # IP Geolocation API (для автодетекта города)
    IPINFO_API_KEY = os.environ.get('IPINFO_API_KEY') or ''

