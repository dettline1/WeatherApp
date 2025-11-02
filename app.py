"""
Weather App - Flask приложение для прогноза погоды
Автор: Daniil
"""
from flask import Flask, render_template, request, jsonify, session
import requests
from config import Config
from database import WeatherDatabase
from translations import get_text, TRANSLATIONS

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db = WeatherDatabase()


def get_weather_data(city, lang='ru'):
    """
    Получение данных о погоде из OpenWeatherMap API
    
    Args:
        city: название города
        lang: язык ответа (ru/en)
    
    Returns:
        dict: данные о погоде или None в случае ошибки
    """
    try:
        params = {
            'q': city,
            'appid': app.config['OPENWEATHER_API_KEY'],
            'units': 'metric',
            'lang': lang
        }
        
        response = requests.get(
            app.config['OPENWEATHER_BASE_URL'],
            params=params,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            weather_info = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'humidity': data['main']['humidity'],
                'wind_speed': round(data['wind']['speed'], 1),
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon'],
                'icon_url': f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            }
            
            # Сохранение в базу данных
            db.add_record(
                weather_info['city'],
                weather_info['country'],
                weather_info['temperature'],
                weather_info['feels_like'],
                weather_info['humidity'],
                weather_info['wind_speed'],
                weather_info['description'],
                weather_info['icon']
            )
            
            return weather_info
        elif response.status_code == 401:
            return {'error': 'error_api_key'}
        elif response.status_code == 404:
            return {'error': 'error_city_not_found'}
        else:
            return {'error': 'error_general'}
            
    except requests.exceptions.RequestException:
        return {'error': 'error_connection'}
    except Exception as e:
        print(f"Error: {e}")
        return {'error': 'error_general'}


def get_city_by_ip():
    """
    Определение города по IP адресу
    
    Returns:
        str: название города или None
    """
    try:
        # Используем ipinfo.io для определения местоположения
        response = requests.get('https://ipinfo.io/json', timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('city', None)
    except:
        pass
    
    return None


@app.route('/')
def index():
    """Главная страница"""
    lang = session.get('language', app.config['DEFAULT_LANGUAGE'])
    
    # Получение истории запросов
    history = db.get_history(limit=5)
    
    return render_template(
        'index.html',
        lang=lang,
        translations=TRANSLATIONS[lang],
        history=history
    )


@app.route('/weather', methods=['POST'])
def weather():
    """API endpoint для получения погоды"""
    data = request.get_json()
    city = data.get('city', '').strip()
    lang = session.get('language', app.config['DEFAULT_LANGUAGE'])
    
    if not city:
        return jsonify({'error': 'error_general'}), 400
    
    weather_data = get_weather_data(city, lang)
    
    if weather_data and 'error' in weather_data:
        return jsonify(weather_data), 400
    
    return jsonify(weather_data)


@app.route('/autodetect', methods=['POST'])
def autodetect():
    """API endpoint для автоопределения города"""
    city = get_city_by_ip()
    
    if city:
        return jsonify({'city': city})
    else:
        return jsonify({'error': 'error_general'}), 400


@app.route('/history')
def history():
    """API endpoint для получения истории"""
    history_data = db.get_history(limit=10)
    return jsonify(history_data)


@app.route('/set_language/<lang>')
def set_language(lang):
    """Установка языка приложения"""
    if lang in app.config['SUPPORTED_LANGUAGES']:
        session['language'] = lang
    return jsonify({'status': 'success', 'language': lang})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

