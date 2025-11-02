# 🔌 API Документация

## Endpoints

### 1. GET `/`
Главная страница приложения

**Ответ:** HTML страница

---

### 2. POST `/weather`
Получение данных о погоде для указанного города

**Request:**
```json
{
  "city": "Moscow"
}
```

**Success Response (200):**
```json
{
  "city": "Moscow",
  "country": "RU",
  "temperature": 5.2,
  "feels_like": 2.1,
  "humidity": 76,
  "wind_speed": 4.5,
  "description": "Облачно с прояснениями",
  "icon": "04d",
  "icon_url": "https://openweathermap.org/img/wn/04d@2x.png"
}
```

**Error Responses:**

```json
// 400 - Город не найден
{
  "error": "error_city_not_found"
}

// 400 - Неверный API ключ
{
  "error": "error_api_key"
}

// 400 - Ошибка соединения
{
  "error": "error_connection"
}

// 400 - Общая ошибка
{
  "error": "error_general"
}
```

---

### 3. POST `/autodetect`
Автоматическое определение города по IP-адресу

**Request:** Пустое тело

**Success Response (200):**
```json
{
  "city": "Moscow"
}
```

**Error Response (400):**
```json
{
  "error": "error_general"
}
```

---

### 4. GET `/history`
Получение истории запросов погоды

**Query Parameters:**
- Нет (по умолчанию последние 10 записей)

**Success Response (200):**
```json
[
  {
    "id": 1,
    "city": "Moscow",
    "country": "RU",
    "temperature": 5.2,
    "feels_like": 2.1,
    "humidity": 76,
    "wind_speed": 4.5,
    "description": "Облачно с прояснениями",
    "icon": "04d",
    "timestamp": "2025-11-02 10:30:45"
  },
  {
    "id": 2,
    "city": "London",
    "country": "GB",
    "temperature": 12.8,
    "feels_like": 11.5,
    "humidity": 82,
    "wind_speed": 3.2,
    "description": "Небольшой дождь",
    "icon": "10d",
    "timestamp": "2025-11-02 10:25:12"
  }
]
```

---

### 5. GET `/set_language/<lang>`
Установка языка интерфейса

**URL Parameters:**
- `lang` - код языка (`ru` или `en`)

**Success Response (200):**
```json
{
  "status": "success",
  "language": "ru"
}
```

---

## Коды погодных иконок

OpenWeatherMap использует следующие коды иконок:

| Код | Описание |
|-----|----------|
| 01d/01n | Ясно |
| 02d/02n | Малооблачно |
| 03d/03n | Облачно |
| 04d/04n | Пасмурно |
| 09d/09n | Ливень |
| 10d/10n | Дождь |
| 11d/11n | Гроза |
| 13d/13n | Снег |
| 50d/50n | Туман |

*d - день, n - ночь*

---

## Коды ошибок

| Ключ ошибки | Описание (RU) | Описание (EN) |
|-------------|---------------|---------------|
| error_city_not_found | Город не найден. Проверьте название. | City not found. Check the name. |
| error_api_key | Ошибка API ключа. Проверьте конфигурацию. | API key error. Check configuration. |
| error_connection | Ошибка подключения к сервису погоды. | Connection error to weather service. |
| error_general | Произошла ошибка. Попробуйте позже. | An error occurred. Try again later. |

---

## Примеры использования

### cURL

**Получение погоды:**
```bash
curl -X POST http://localhost:5000/weather \
  -H "Content-Type: application/json" \
  -d '{"city":"Moscow"}'
```

**Автоопределение города:**
```bash
curl -X POST http://localhost:5000/autodetect
```

**Получение истории:**
```bash
curl http://localhost:5000/history
```

**Смена языка:**
```bash
curl http://localhost:5000/set_language/en
```

### Python

```python
import requests

# Получение погоды
response = requests.post(
    'http://localhost:5000/weather',
    json={'city': 'Moscow'}
)
data = response.json()
print(f"Температура в {data['city']}: {data['temperature']}°C")

# Автоопределение
response = requests.post('http://localhost:5000/autodetect')
city = response.json()['city']
print(f"Ваш город: {city}")

# История
response = requests.get('http://localhost:5000/history')
history = response.json()
for item in history:
    print(f"{item['city']}: {item['temperature']}°C - {item['timestamp']}")
```

### JavaScript (Fetch API)

```javascript
// Получение погоды
async function getWeather(city) {
  const response = await fetch('/weather', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ city: city })
  });
  
  const data = await response.json();
  return data;
}

// Автоопределение
async function autodetect() {
  const response = await fetch('/autodetect', {
    method: 'POST'
  });
  
  const data = await response.json();
  return data.city;
}

// История
async function getHistory() {
  const response = await fetch('/history');
  const data = await response.json();
  return data;
}

// Использование
getWeather('Moscow').then(data => {
  console.log(`Temperature: ${data.temperature}°C`);
});
```

---

## Rate Limits

**OpenWeatherMap Free Plan:**
- 60 запросов в минуту
- 1,000,000 запросов в месяц

**ipinfo.io Free Plan:**
- 50,000 запросов в месяц

---

## База данных

### Таблица: weather_history

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Первичный ключ (автоинкремент) |
| city | TEXT | Название города |
| country | TEXT | Код страны |
| temperature | REAL | Температура в °C |
| feels_like | REAL | Ощущаемая температура в °C |
| humidity | INTEGER | Влажность в % |
| wind_speed | REAL | Скорость ветра в м/с |
| description | TEXT | Описание погоды |
| icon | TEXT | Код иконки |
| timestamp | DATETIME | Время запроса (автоматически) |

---

**Weather App API by Daniil** © 2025

