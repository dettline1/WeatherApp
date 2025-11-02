"""
Переводы для многоязычной поддержки
"""

TRANSLATIONS = {
    'ru': {
        'app_title': 'Прогноз Погоды',
        'search_placeholder': 'Введите название города...',
        'search_button': 'Показать погоду',
        'temperature': 'Температура',
        'feels_like': 'Ощущается как',
        'humidity': 'Влажность',
        'wind_speed': 'Скорость ветра',
        'history_title': 'История запросов',
        'no_history': 'История пуста',
        'error_city_not_found': 'Город не найден. Проверьте название.',
        'error_api_key': 'Ошибка API ключа. Проверьте конфигурацию.',
        'error_connection': 'Ошибка подключения к сервису погоды.',
        'error_general': 'Произошла ошибка. Попробуйте позже.',
        'autodetect': 'Определить мой город',
        'language': 'Язык',
        'footer': 'Weather App by Daniil',
        'last_updated': 'Обновлено',
        'clear_history': 'Очистить историю'
    },
    'en': {
        'app_title': 'Weather Forecast',
        'search_placeholder': 'Enter city name...',
        'search_button': 'Show Weather',
        'temperature': 'Temperature',
        'feels_like': 'Feels Like',
        'humidity': 'Humidity',
        'wind_speed': 'Wind Speed',
        'history_title': 'Search History',
        'no_history': 'No history yet',
        'error_city_not_found': 'City not found. Check the name.',
        'error_api_key': 'API key error. Check configuration.',
        'error_connection': 'Connection error to weather service.',
        'error_general': 'An error occurred. Try again later.',
        'autodetect': 'Detect my city',
        'language': 'Language',
        'footer': 'Weather App by Daniil',
        'last_updated': 'Updated',
        'clear_history': 'Clear History'
    }
}

def get_text(key, lang='ru'):
    """Получить перевод по ключу"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['ru']).get(key, key)

