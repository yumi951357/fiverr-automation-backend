from flask import Flask, jsonify, request
from flask_cors import CORS  # 添加 CORS 支持
import os
import datetime

app = Flask(__name__)

# 添加 CORS 支持，允许所有前端域名
CORS(app, origins=[
    "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
    "https://frontend-nib8wfau8-yumi951357s-projects.vercel.app", 
    "https://frontend-pmxc6gltj-yumi951357s-projects.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
])

@app.route('/')
def index():
    return jsonify({
        "status": "ok", 
        "service": "Fiverr AI Automation Backend",
        "timestamp": str(datetime.datetime.utcnow())
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['POST'])
def tasks():
    data = request.get_json(force=True)
    return jsonify({
        "result": "success",
        "task": data.get('type'),
        "payload": data.get('payload', {}),
        "processed_at": str(datetime.datetime.utcnow())
    })

@app.route('/api/audit', methods=['POST'])
def audit():
    data = request.get_json(force=True)
    return jsonify({
        "determinacy_score": 0.95,
        "deception_probability": 0.02,
        "ethical_weight": 0.87,
        "audit_hash": "verifiable_hash_" + str(datetime.datetime.utcnow().timestamp()),
        "timestamp": str(datetime.datetime.utcnow())
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)