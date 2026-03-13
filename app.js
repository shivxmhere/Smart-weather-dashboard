function calculateComfortScore(temp, humidity, wind_speed) {
    let score = 100;

    // Temperature penalty (ideal: 20-28°C)
    if (temp < 15) {
        score -= (15 - temp) * 3;
    } else if (temp > 35) {
        score -= (temp - 35) * 4;
    } else if (temp >= 20 && temp <= 28) {
        score += 10;
    }

    // Humidity penalty (ideal: 40-60%)
    if (humidity > 70) {
        score -= (humidity - 70) * 0.5;
    } else if (humidity < 30) {
        score -= (30 - humidity) * 0.3;
    }

    // Wind penalty (ideal: < 20 km/h)
    if (wind_speed > 20) {
        score -= (wind_speed - 20) * 1.5;
    }

    return Math.max(0, Math.min(100, Math.round(score)));
}

async function fetchWeather(city) {
    const dashboard = document.getElementById('dashboard');
    const loader = document.getElementById('loader');
    
    dashboard.style.display = 'none';
    loader.style.display = 'block';

    try {
        const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
        const data = await response.json();

        if (data.error) throw new Error(data.error);

        renderDashboard(data);
    } catch (error) {
        console.error('Error fetching weather:', error);
        alert('Failed to fetch weather data. Please try again later.');
    } finally {
        loader.style.display = 'none';
    }
}

function renderDashboard(data) {
    const dashboard = document.getElementById('dashboard');
    const hourlyGrid = document.getElementById('hourlyGrid');
    const cityNameDisplay = document.getElementById('cityNameDisplay');
    const avgScoreDisplay = document.getElementById('avgScore');
    const bestWindowDisplay = document.getElementById('bestWindowText');

    cityNameDisplay.textContent = data.city;
    hourlyGrid.innerHTML = '';

    let totalScore = 0;
    let scores = [];

    data.hourly.forEach((h, index) => {
        const score = calculateComfortScore(h.temp, h.humidity, h.wind_speed);
        totalScore += score;
        scores.push({ time: h.time, score: score });

        const card = document.createElement('div');
        card.className = 'weather-card';
        card.style.animationDelay = `${index * 0.1}s`;

        const date = new Date(h.time);
        const timeStr = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        card.innerHTML = `
            <div class="card-time">${timeStr}</div>
            <div class="card-temp">${Math.round(h.temp)}°C</div>
            <div class="card-desc">${h.description}</div>
            <div class="card-stats">
                <span>💧 Humidity: ${h.humidity}%</span>
                <span>🌬️ Wind: ${h.wind_speed} km/h</span>
                <span style="color: ${getScoreColor(score)}; font-weight: 700;">Comfort: ${score}/100</span>
            </div>
        `;
        hourlyGrid.appendChild(card);
    });

    const avgScore = Math.round(totalScore / data.hourly.length);
    avgScoreDisplay.textContent = `${avgScore}/100`;
    avgScoreDisplay.style.color = getScoreColor(avgScore);

    // Find best window
    const bestOne = scores.reduce((prev, current) => (prev.score > current.score) ? prev : current);
    bestWindowDisplay.textContent = `${new Date(bestOne.time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} with a score of ${bestOne.score}!`;

    dashboard.style.display = 'grid';
}

function getScoreColor(score) {
    if (score >= 75) return '#4ade80';
    if (score >= 50) return '#facc15';
    return '#f87171';
}

document.getElementById('searchBtn').addEventListener('click', () => {
    const city = document.getElementById('cityInput').value.trim();
    if (city) fetchWeather(city);
});

document.getElementById('cityInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const city = e.target.value.trim();
        if (city) fetchWeather(city);
    }
});

// Initial Load
fetchWeather('Delhi');
