const metricTimeElement = document.getElementById('metric-time');
const localTimeElement = document.getElementById('local-time');
const toggleModeButton = document.getElementById('toggle-mode');
const bodyElement = document.body;

function updateTimes() {
    const now = new Date();

    // Convert to metric time
    const metricHourRatio = 10 / 24;
    const hours = now.getUTCHours() + now.getUTCMinutes() / 60 + now.getUTCSeconds() / 3600;
    const metricTime = hours * metricHourRatio;
    const metricHours = Math.floor(metricTime);
    const metricMinutes = Math.floor((metricTime - metricHours) * 100);
    const metricSeconds = Math.floor(((metricTime - metricHours) * 100 - metricMinutes) * 100);

    // Update metric time display
    metricTimeElement.textContent = `${metricHours.toString().padStart(2, '0')}:${metricMinutes.toString().padStart(2, '0')}:${metricSeconds.toString().padStart(2, '0')}`;

    // Update local time display
    const localHours = now.getHours();
    const localMinutes = now.getMinutes();
    const localSeconds = now.getSeconds();
    localTimeElement.textContent = `${localHours.toString().padStart(2, '0')}:${localMinutes.toString().padStart(2, '0')}:${localSeconds.toString().padStart(2, '0')}`;
}

function toggleMode() {
    bodyElement.classList.toggle('dark-mode');
}

toggleModeButton.addEventListener('click', toggleMode);

// Update time every second
setInterval(updateTimes, 200);

// Initialize
updateTimes();
