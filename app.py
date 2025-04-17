from flask import Flask, jsonify
from threading import Thread
from sniffer import start_sniffing, captured_data  # Import from sniffer.py

app = Flask(__name__)

@app.route('/start_sniffing', methods=['GET'])
def start_sniffing_route():
    sniff_thread = Thread(target=start_sniffing)
    sniff_thread.daemon = True
    sniff_thread.start()
    return jsonify({"status": "Sniffing started"}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(captured_data), 200

@app.route('/stop_sniffing', methods=['GET'])
def stop_sniffing():
    # Ideally, we would implement a method to stop sniffing here
    return jsonify({"status": "Sniffing stopped (manual implementation required)"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
