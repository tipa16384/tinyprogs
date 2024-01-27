// function to draw a metric clock on the canvas with the id 'clock'. The elapsed portion should be draw in gray.
function mt_drawClock() {
    const canvas = document.getElementById('mt_clock');
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

// Update time every tenth of a second
setInterval(mt_drawClock, 100);
