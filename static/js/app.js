// Weather App JavaScript

// Глобальные переменные
let currentTranslations = translations || {};

// Поиск погоды по названию города
async function searchWeather() {
    const cityInput = document.getElementById('cityInput');
    const city = cityInput.value.trim();
    
    if (!city) {
        showError(currentTranslations.error_general);
        return;
    }
    
    showLoading(true);
    hideError();
    hideWeatherCard();
    
    try {
        const response = await fetch('/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city: city })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayWeather(data);
        } else {
            showError(currentTranslations[data.error] || currentTranslations.error_general);
        }
    } catch (error) {
        showError(currentTranslations.error_connection);
    } finally {
        showLoading(false);
    }
}

// Поиск погоды по имени из истории
function searchWeatherByName(city) {
    document.getElementById('cityInput').value = city;
    searchWeather();
}

// Автоопределение города по IP
async function autodetectCity() {
    const autodetectBtn = document.getElementById('autodetectBtn');
    const originalText = autodetectBtn.innerHTML;
    
    autodetectBtn.disabled = true;
    autodetectBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Loading...';
    
    try {
        const response = await fetch('/autodetect', {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (response.ok && data.city) {
            document.getElementById('cityInput').value = data.city;
            searchWeather();
        } else {
            showError(currentTranslations.error_general);
        }
    } catch (error) {
        showError(currentTranslations.error_connection);
    } finally {
        autodetectBtn.disabled = false;
        autodetectBtn.innerHTML = originalText;
    }
}

// Отображение данных о погоде
function displayWeather(data) {
    document.getElementById('weatherIcon').src = data.icon_url;
    document.getElementById('weatherIcon').alt = data.description;
    document.getElementById('cityName').textContent = `${data.city}, ${data.country}`;
    document.getElementById('weatherDescription').textContent = data.description;
    document.getElementById('temperature').textContent = `${data.temperature}°C`;
    document.getElementById('feelsLike').textContent = `${data.feels_like}°C`;
    document.getElementById('humidity').textContent = `${data.humidity}%`;
    document.getElementById('windSpeed').textContent = `${data.wind_speed} м/с`;
    
    showWeatherCard();
}

// Показать/скрыть карточку погоды
function showWeatherCard() {
    document.getElementById('weatherCard').classList.remove('d-none');
}

function hideWeatherCard() {
    document.getElementById('weatherCard').classList.add('d-none');
}

// Показать/скрыть загрузку
function showLoading(show) {
    const spinner = document.getElementById('loadingSpinner');
    if (show) {
        spinner.classList.remove('d-none');
    } else {
        spinner.classList.add('d-none');
    }
}

// Показать/скрыть ошибку
function showError(message) {
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorAlert.classList.remove('d-none');
    
    // Автоматически скрыть через 5 секунд
    setTimeout(() => {
        hideError();
    }, 5000);
}

function hideError() {
    document.getElementById('errorAlert').classList.add('d-none');
}

// Установка языка
async function setLanguage(lang) {
    try {
        const response = await fetch(`/set_language/${lang}`);
        
        if (response.ok) {
            // Перезагрузка страницы для применения нового языка
            location.reload();
        }
    } catch (error) {
        console.error('Error setting language:', error);
    }
}

// Обработка нажатия Enter в поле ввода
document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    
    if (cityInput) {
        cityInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchWeather();
            }
        });
        
        // Фокус на поле ввода при загрузке
        cityInput.focus();
    }
});

