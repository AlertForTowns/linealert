from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    snapshot_file = 'decrypted_snapshot.json'
    if not os.path.exists(snapshot_file):
        return "<h1>No snapshot found</h1>"

    with open(snapshot_file) as f:
        data = json.load(f)

    return render_template_string('''
        <h1 style="font-family:sans-serif;">📊 LineAlert Snapshot Viewer</h1>
        <p><strong>📅 Timestamp:</strong> {{ data['timestamp'] }}</p>
        <p><strong>🖥️ Device:</strong> {{ data['device'] }}</p>
        <p><strong>🔌 Protocol:</strong> {{ data['protocol'] }}</p>
        <p><strong>⚠️ Event:</strong> {{ data['event'] }}</p>
        <p><strong>🚨 Severity:</strong> {{ data['severity'] }}</p>
    ''', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
