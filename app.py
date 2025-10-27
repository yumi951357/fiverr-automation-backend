from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'status':'ok'})

@app.route('/tasks', methods=['POST'])
def tasks():
    data = request.get_json(force=True)
    return jsonify({'task': data.get('type'), 'payload': data.get('payload', {})})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)