#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для быстрого запуска Weather App
"""

import os
import sys

def check_api_key():
    """Проверка наличия API ключа"""
    from config import Config
    
    if Config.OPENWEATHER_API_KEY == 'YOUR_API_KEY_HERE':
        print("⚠️  ВНИМАНИЕ: API ключ не настроен!")
        print("\nДля работы приложения необходимо:")
        print("1. Получить API ключ на https://openweathermap.org/api")
        print("2. Установить переменную окружения:")
        print("   set OPENWEATHER_API_KEY=ваш_ключ (Windows)")
        print("   export OPENWEATHER_API_KEY=ваш_ключ (Linux/Mac)")
        print("\nИли отредактировать config.py и заменить YOUR_API_KEY_HERE на ваш ключ\n")
        
        choice = input("Продолжить без API ключа? (y/n): ")
        if choice.lower() != 'y':
            sys.exit(0)

def main():
    """Главная функция запуска"""
    print("=" * 50)
    print("🌤️  Weather App by Daniil")
    print("=" * 50)
    
    # Проверка зависимостей
    try:
        import flask
        import requests
    except ImportError:
        print("\n❌ Не установлены зависимости!")
        print("Выполните: pip install -r requirements.txt\n")
        sys.exit(1)
    
    # Проверка API ключа
    check_api_key()
    
    # Запуск приложения
    print("\n✅ Запуск приложения...")
    print("🌐 Приложение будет доступно по адресу: http://localhost:5000")
    print("📝 Нажмите Ctrl+C для остановки\n")
    
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()

