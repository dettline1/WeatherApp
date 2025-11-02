#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт первоначальной настройки Weather App
"""

import os
import sys
import subprocess

def print_header():
    """Красивый заголовок"""
    print("\n" + "=" * 60)
    print("🌤️  Weather App - Мастер установки")
    print("=" * 60 + "\n")


def check_python_version():
    """Проверка версии Python"""
    print("🐍 Проверка версии Python...")
    
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} не поддерживается")
        print("   Требуется Python 3.8 или выше")
        return False


def install_dependencies():
    """Установка зависимостей"""
    print("\n📦 Установка зависимостей...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Зависимости установлены!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Ошибка установки зависимостей")
        return False


def setup_api_key():
    """Настройка API ключа"""
    print("\n🔑 Настройка OpenWeatherMap API ключа...")
    
    print("\nДля работы приложения нужен API ключ от OpenWeatherMap.")
    print("Получить бесплатный ключ: https://openweathermap.org/api\n")
    
    choice = input("У вас есть API ключ? (y/n): ").lower()
    
    if choice == 'y':
        api_key = input("Введите ваш API ключ: ").strip()
        
        if api_key:
            # Создание .env файла
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(f"OPENWEATHER_API_KEY={api_key}\n")
            
            print("✅ API ключ сохранен в .env файле!")
            return True
        else:
            print("⚠️  API ключ не введен. Настройте позже в config.py или .env")
            return False
    else:
        print("\n📋 Инструкция:")
        print("1. Перейдите на https://openweathermap.org/api")
        print("2. Зарегистрируйтесь и получите бесплатный API ключ")
        print("3. Запустите setup.py снова или отредактируйте config.py")
        return False


def create_env_file():
    """Создание .env файла из примера"""
    print("\n📄 Создание файла переменных окружения...")
    
    if os.path.exists('.env'):
        print("⚠️  Файл .env уже существует")
        return True
    
    if os.path.exists('.env.example'):
        try:
            with open('.env.example', 'r', encoding='utf-8') as src:
                content = src.read()
            
            with open('.env', 'w', encoding='utf-8') as dst:
                dst.write(content)
            
            print("✅ Создан .env файл из .env.example")
            return True
        except Exception as e:
            print(f"❌ Ошибка создания .env: {e}")
            return False
    else:
        print("⚠️  Файл .env.example не найден")
        return False


def initialize_database():
    """Инициализация базы данных"""
    print("\n🗄️  Инициализация базы данных...")
    
    try:
        from database import WeatherDatabase
        
        db = WeatherDatabase()
        print("✅ База данных инициализирована!")
        return True
    except Exception as e:
        print(f"❌ Ошибка инициализации БД: {e}")
        return False


def run_tests():
    """Запуск тестов"""
    print("\n🧪 Запуск тестов...")
    
    try:
        result = subprocess.call([sys.executable, "test_api.py"])
        if result == 0:
            print("✅ Все тесты пройдены!")
            return True
        else:
            print("⚠️  Некоторые тесты не пройдены")
            return False
    except Exception as e:
        print(f"⚠️  Не удалось запустить тесты: {e}")
        return False


def print_next_steps():
    """Следующие шаги"""
    print("\n" + "=" * 60)
    print("🎉 Установка завершена!")
    print("=" * 60)
    
    print("\n📋 Следующие шаги:")
    print("\n1. Если вы еще не настроили API ключ:")
    print("   - Получите ключ на https://openweathermap.org/api")
    print("   - Добавьте в .env файл: OPENWEATHER_API_KEY=ваш_ключ")
    
    print("\n2. Запустите приложение:")
    print("   python run.py")
    
    print("\n3. Откройте в браузере:")
    print("   http://localhost:5000")
    
    print("\n4. Документация:")
    print("   - README.md - основная документация")
    print("   - QUICKSTART.md - быстрый старт")
    print("   - FEATURES.md - список функций")
    print("   - API_DOCUMENTATION.md - API документация")
    
    print("\n🌟 Приятного использования!")
    print("\n")


def main():
    """Главная функция"""
    print_header()
    
    steps = [
        ("Проверка Python", check_python_version),
        ("Установка зависимостей", install_dependencies),
        ("Инициализация БД", initialize_database),
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print(f"\n❌ Ошибка на этапе: {step_name}")
            print("Установка прервана. Исправьте ошибки и запустите снова.")
            return 1
    
    # Опциональные шаги
    setup_api_key()
    run_tests()
    
    print_next_steps()
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Установка прервана пользователем")
        sys.exit(1)

