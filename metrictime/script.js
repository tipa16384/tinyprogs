const metricTimeElement = document.getElementById('metric-time');
const localTimeElement = document.getElementById('local-time');
const toggleModeButton = document.getElementById('toggle-mode');
const bodyElement = document.body;

// make a list of tuples where the left element is the name of an event, like 'breakfast', 'bedtime', 'work', etc,
// and the right element is the time of the day in local time when that event happens
const events = [
    ['breakfast', 6.5],
    ['lunch', 12],
    ['dinner', 18],
    ['bedtime', 23],
    ['work', 8.5],
    ['end of work', 17.5]
];

// function to insert the table of events and their times in metric time as the content of the table with id 'event-table'
function insertEventTable() {
    // sort events in ascending order by the time
    events.sort((a, b) => a[1] - b[1]);
    const table = document.getElementById('event-table');
    for (let i = 0; i < events.length; i++) {
        const row = table.insertRow(i);
        const eventCell = row.insertCell(0);
        const timeCell = row.insertCell(1);
        eventCell.innerHTML = events[i][0];
        timeCell.innerHTML = localToMetricTime(events[i][1]);
    }
}

// function to draw a metric clock on the canvas with the id 'clock'. The elapsed portion should be draw in gray.
function drawClock() {
    const canvas = document.getElementById('clock');
    const context = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const radius = Math.min(width, height) / 2 * 0.9;
    const center = {x: width / 2, y: height / 2};
    const now = new Date();

    // Convert to metric time
    const metricHourRatio = 10 / 24;
    const hours = now.getHours() + now.getMinutes() / 60 + now.getSeconds() / 3600 + now.getMilliseconds() / 3600000;
    const metricTime = hours * metricHourRatio;
    const metricHours = metricTime;
    const metricMinutes = (metricTime - Math.floor(metricHours)) * 100;
    const metricSeconds = ((metricTime - Math.floor(metricHours)) * 100 - Math.floor(metricMinutes)) * 100;

    // Draw background
    context.fillStyle = '#ffffff';
    context.fillRect(0, 0, width, height);

    // draw a solid circle for the clock face and fill it with light gray
    context.fillStyle = '#eeeeee';
    context.beginPath();
    context.arc(center.x, center.y, radius, 0, 2 * Math.PI);
    context.fill();

    


    // Draw clock face
    context.strokeStyle = '#000000';
    context.lineWidth = 10;
    context.beginPath();
    context.arc(center.x, center.y, radius, -Math.PI/2, 2 * Math.PI - Math.PI/2);
    context.stroke();

    // Draw hours
    context.strokeStyle = '#aaaa00';
    context.lineWidth = 10;
    context.beginPath();
    context.arc(center.x, center.y, radius * 0.9, -Math.PI/2, 2 * Math.PI * metricHours / 10-Math.PI/2);
    context.stroke();

    // Draw minutes
    context.strokeStyle = '#cccc00';
    context.lineWidth = 10;
    context.beginPath();
    context.arc(center.x, center.y, radius * 0.8, -Math.PI/2, 2 * Math.PI * metricMinutes / 100-Math.PI/2);
    context.stroke();

    // Draw seconds in orange

    context.strokeStyle = '#ff8800';
    context.lineWidth = 10;
    context.beginPath();
    context.arc(center.x, center.y, radius * 0.7, -Math.PI/2, 2 * Math.PI * metricSeconds / 100-Math.PI/2);
    context.stroke();

    // draw the metric time in hh:mm:ss format in the center of the clock face
    context.fillStyle = '#000000';
    context.font = '28px sans-serif';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.fillText(`${Math.floor(metricHours).toString().padStart(2, '0')}:${Math.floor(metricMinutes).toString().padStart(2, '0')}:${Math.floor(metricSeconds).toString().padStart(2, '0')}`, center.x, center.y);

    // local time rendered beneath it in a smaller font
    context.fillStyle = '#000000';
    context.font = '14px sans-serif';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.fillText(`${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`, center.x, center.y + 30);

}

// function that takes an hour (0-23) in local time and returns the corresponding time in metric time as a string in hh:mm format.
function localToMetricTime(localHour) {
    const metricHourRatio = 10 / 24;
    const metricTime = localHour * metricHourRatio;
    const metricHours = Math.floor(metricTime);
    const metricMinutes = Math.floor((metricTime - metricHours) * 100);
    return `${metricHours.toString().padStart(2, '0')}:${metricMinutes.toString().padStart(2, '0')}`;
}



function updateTimes() {
    const now = new Date();

    // Convert to metric time
    const metricHourRatio = 10 / 24;
//    const hours = now.getUTCHours() + now.getUTCMinutes() / 60 + now.getUTCSeconds() / 3600;
    const hours = now.getHours() + now.getMinutes() / 60 + now.getSeconds() / 3600 + now.getMilliseconds() / 3600000;
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

    drawClock();
}

function toggleMode() {
    bodyElement.classList.toggle('dark-mode');
}

toggleModeButton.addEventListener('click', toggleMode);

// Update time every second
setInterval(updateTimes, 100);

// Initialize
updateTimes();
insertEventTable();
drawClock();
