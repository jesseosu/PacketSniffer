// DOM Elements
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const packetDataDiv = document.getElementById('packetData');

// Event Listener for "Start Sniffing" Button
startBtn.addEventListener('click', function() {
    fetch('http://localhost:5000/start_sniffing')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert("Packet Sniffer Started!");
            startBtn.disabled = true;
            stopBtn.disabled = false;
        })
        .catch(error => console.error('Error starting sniffer:', error));
});

// Event Listener for "Stop Sniffing" Button
stopBtn.addEventListener('click', function() {
    fetch('http://localhost:5000/stop_sniffing')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert("Packet Sniffer Stopped!");
            startBtn.disabled = false;
            stopBtn.disabled = true;
        })
        .catch(error => console.error('Error stopping sniffer:', error));
});

// Function to fetch and display captured data
function fetchCapturedData() {
    fetch('http://localhost:5000/get_data')
        .then(response => response.json())
        .then(data => {
            packetDataDiv.innerHTML = ''; // Clear previous data

            // Check if there is no data captured yet
            if (data.length === 0) {
                packetDataDiv.innerHTML = '<p>No data captured yet.</p>';
            } else {
                data.forEach(packet => {
                    const packetElement = document.createElement('div');
                    packetElement.classList.add('packet');
                    packetElement.innerHTML = `
                        <strong>Timestamp:</strong> ${packet.timestamp} <br>
                        <strong>Protocol:</strong> ${packet.protocol} <br>
                        <strong>Domain:</strong> ${packet.domain} <br>
                        <strong>IP:</strong> ${packet.ip}
                    `;
                    packetDataDiv.appendChild(packetElement);
                });
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Fetch data every 2 seconds
setInterval(fetchCapturedData, 2000);
