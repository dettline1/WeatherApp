#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для тестирования Weather App API
"""

import sys
import requests
from config import Config

def test_api_key():
    """Проверка валидности API ключа OpenWeatherMap"""
    print("🔑 Проверка API ключа OpenWeatherMap...")
    
    api_key = Config.OPENWEATHER_API_KEY
    
    if api_key == 'YOUR_API_KEY_HERE':
        print("❌ API ключ не настроен!")
        print("   Установите переменную окружения OPENWEATHER_API_KEY")
        return False
    
    try:
        # Тестовый запрос к API
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={
                'q': 'London',
                'appid': api_key,
                'units': 'metric'
            },
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ API ключ валиден!")
            data = response.json()
            print(f"   Тестовый запрос: {data['name']}, {data['main']['temp']}°C")
            return True
        elif response.status_code == 401:
            print("❌ API ключ невалиден!")
            print("   Проверьте правильность ключа")
            return False
        else:
            print(f"⚠️  Неожиданный ответ: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False


def test_database():
    """Проверка работы с базой данных"""
    print("\n🗄️  Проверка базы данных...")
    
    try:
        from database import WeatherDatabase
        
        db = WeatherDatabase()
        
        # Тестовая запись
        db.add_record(
            city='Test City',
            country='TC',
            temperature=20.5,
            feels_like=18.2,
            humidity=65,
            wind_speed=3.5,
            description='Test weather',
            icon='01d'
        )
        
        # Чтение истории
        history = db.get_history(limit=1)
        
        if history:
            print("✅ База данных работает!")
            print(f"   Последняя запись: {history[0]['city']}")
            return True
        else:
            print("⚠️  База данных пуста")
            return True
            
    except Exception as e:
        print(f"❌ Ошибка базы данных: {e}")
        return False


def test_translations():
    """Проверка переводов"""
    print("\n🌐 Проверка переводов...")
    
    try:
        from translations import TRANSLATIONS, get_text
        
        # Проверка наличия всех ключей
        required_keys = [
            'app_title', 'search_placeholder', 'search_button',
            'temperature', 'humidity', 'wind_speed'
        ]
        
        for lang in ['ru', 'en']:
            missing_keys = []
            for key in required_keys:
                if key not in TRANSLATIONS[lang]:
                    missing_keys.append(key)
            
            if missing_keys:
                print(f"⚠️  Отсутствуют ключи для {lang}: {missing_keys}")
            else:
                print(f"✅ Переводы {lang.upper()} в порядке!")
        
        # Проверка функции get_text
        text = get_text('app_title', 'ru')
        if text:
            print(f"   Пример: app_title (RU) = '{text}'")
            return True
        else:
            print("❌ Функция get_text не работает")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка переводов: {e}")
        return False


def test_flask_import():
    """Проверка импорта Flask приложения"""
    print("\n🌶️  Проверка Flask приложения...")
    
    try:
        from app import app
        
        if app:
            print("✅ Flask приложение загружено!")
            print(f"   Секретный ключ установлен: {bool(app.config['SECRET_KEY'])}")
            return True
        else:
            print("❌ Не удалось загрузить Flask приложение")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка импорта: {e}")
        return False


def main():
    """Главная функция тестирования"""
    print("=" * 60)
    print("🧪 Weather App - Тестирование компонентов")
    print("=" * 60)
    
    tests = [
        test_api_key,
        test_database,
        test_translations,
        test_flask_import
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    # Итоги
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Результаты: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("✅ Все тесты пройдены! Приложение готово к запуску.")
        print("\n🚀 Запустите: python run.py")
        return 0
    else:
        print("⚠️  Некоторые тесты не пройдены. Проверьте настройки.")
        return 1


if __name__ == '__main__':
    sys.exit(main())

