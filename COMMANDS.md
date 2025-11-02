# ⌨️ Шпаргалка по командам

## 🚀 Быстрый старт

```bash
# Клонирование (если из GitHub)
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/Mac)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск мастера установки
python setup.py

# Запуск приложения
python run.py
```

## 📦 Управление зависимостями

```bash
# Установка всех зависимостей
pip install -r requirements.txt

# Обновление зависимостей
pip install --upgrade -r requirements.txt

# Добавление новой зависимости
pip install package_name
pip freeze > requirements.txt

# Проверка установленных пакетов
pip list
```

## 🧪 Тестирование

```bash
# Запуск тестов компонентов
python test_api.py

# Проверка импортов
python -c "from app import app; print('OK')"

# Проверка базы данных
python -c "from database import WeatherDatabase; db = WeatherDatabase(); print('DB OK')"
```

## ▶️ Запуск приложения

```bash
# Обычный запуск
python app.py

# Запуск через run.py (с проверками)
python run.py

# Запуск на другом порту
# Отредактируйте app.py: app.run(port=8000)
python app.py

# Запуск в production режиме
export FLASK_ENV=production  # Linux/Mac
set FLASK_ENV=production     # Windows
python app.py
```

## 🔧 Настройка

```bash
# Установка API ключа через переменную окружения

# Windows
set OPENWEATHER_API_KEY=ваш_ключ_здесь

# Linux/Mac
export OPENWEATHER_API_KEY=ваш_ключ_здесь

# PowerShell
$env:OPENWEATHER_API_KEY="ваш_ключ_здесь"

# Постоянная установка (Linux/Mac)
echo 'export OPENWEATHER_API_KEY=ваш_ключ' >> ~/.bashrc
source ~/.bashrc
```

## 🗄️ База данных

```bash
# Создание новой базы данных
python -c "from database import WeatherDatabase; WeatherDatabase()"

# Просмотр истории (через Python)
python -c "from database import WeatherDatabase; db = WeatherDatabase(); print(db.get_history())"

# Удаление базы данных
rm weather_history.db      # Linux/Mac
del weather_history.db     # Windows

# Пересоздание базы данных
python -c "from database import WeatherDatabase; WeatherDatabase().init_db()"
```

## 📝 Git команды

```bash
# Инициализация репозитория
git init

# Добавление файлов
git add .

# Первый коммит
git commit -m "Initial commit: Weather App v1.0.0"

# Создание .gitignore (если не создан)
# Добавьте: venv/, *.db, __pycache__/, .env

# Связь с GitHub
git remote add origin https://github.com/yourusername/weather-app.git

# Первый push
git branch -M main
git push -u origin main

# Последующие коммиты
git add .
git commit -m "Update: Description"
git push
```

## 🌿 Работа с ветками

```bash
# Создание новой ветки
git checkout -b feature/new-feature

# Переключение между ветками
git checkout main
git checkout feature/new-feature

# Слияние ветки
git checkout main
git merge feature/new-feature

# Удаление ветки
git branch -d feature/new-feature
```

## 🐳 Docker (опционально)

```bash
# Создание Dockerfile
cat > Dockerfile << EOF
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
EOF

# Сборка образа
docker build -t weather-app .

# Запуск контейнера
docker run -p 5000:5000 -e OPENWEATHER_API_KEY=ваш_ключ weather-app

# Остановка контейнера
docker stop $(docker ps -q --filter ancestor=weather-app)
```

## 🚀 Деплой на Heroku

```bash
# Установка Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Вход в Heroku
heroku login

# Создание приложения
heroku create your-weather-app-name

# Создание Procfile
echo "web: gunicorn app:app" > Procfile

# Установка gunicorn
pip install gunicorn
pip freeze > requirements.txt

# Установка переменных окружения
heroku config:set OPENWEATHER_API_KEY=ваш_ключ

# Деплой
git push heroku main

# Открыть приложение
heroku open

# Просмотр логов
heroku logs --tail
```

## 🔍 Отладка

```bash
# Запуск с отладкой
python -m pdb app.py

# Проверка синтаксиса
python -m py_compile app.py

# Просмотр логов Flask
# Логи выводятся в консоль при debug=True

# Проверка портов
netstat -an | findstr :5000    # Windows
lsof -i :5000                  # Linux/Mac

# Убить процесс на порту 5000 (если занят)
# Linux/Mac:
kill -9 $(lsof -t -i:5000)
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

## 📊 Мониторинг

```bash
# Просмотр запущенных процессов Python
ps aux | grep python          # Linux/Mac
tasklist | findstr python.exe # Windows

# Использование памяти
# Linux/Mac
ps -o pid,vsz,rss,comm -C python

# Использование CPU
top -p $(pgrep -f "python app.py")
```

## 🧹 Очистка

```bash
# Очистка кэша Python
find . -type d -name __pycache__ -exec rm -r {} +  # Linux/Mac
for /d /r %i in (__pycache__) do @rd /s /q "%i"    # Windows

# Очистка .pyc файлов
find . -name "*.pyc" -delete   # Linux/Mac
del /s /q *.pyc               # Windows

# Удаление виртуального окружения
rm -rf venv    # Linux/Mac
rmdir /s venv  # Windows

# Полная очистка и переустановка
rm -rf venv __pycache__ *.db
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
```

## 📚 Полезные команды Python

```bash
# Проверка версии Python
python --version

# Проверка версии pip
pip --version

# Обновление pip
python -m pip install --upgrade pip

# Интерактивная консоль Python
python

# Выполнение Python кода из командной строки
python -c "print('Hello, World!')"

# Запуск модуля как скрипт
python -m http.server 8000  # Пример: запуск HTTP сервера
```

## 🔐 Безопасность

```bash
# Генерация секретного ключа
python -c "import secrets; print(secrets.token_hex(32))"

# Проверка зависимостей на уязвимости (требуется safety)
pip install safety
safety check

# Аудит зависимостей
pip-audit  # требуется pip-audit
```

## 📖 Документация

```bash
# Просмотр документации в браузере
python -m pydoc -b

# Документация конкретного модуля
python -m pydoc flask

# Создание документации (если используете Sphinx)
sphinx-quickstart
sphinx-build -b html docs/ docs/_build/
```

## 🎯 Одной командой

```bash
# Полная установка и запуск (Linux/Mac)
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python setup.py && python run.py

# Полная установка и запуск (Windows)
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python setup.py && python run.py
```

---

## 💡 Советы

1. **Всегда используйте виртуальное окружение**
2. **Регулярно обновляйте зависимости**
3. **Делайте коммиты часто и с понятными сообщениями**
4. **Тестируйте перед деплоем**
5. **Храните API ключи в переменных окружения**
6. **Используйте .gitignore для исключения файлов**

---

**Weather App Command Reference** © 2025

