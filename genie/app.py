from flask import Flask, request, jsonify
import requests
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
DEVICE_ID = os.getenv("DEVICE_ID")

BASE_URL = "https://genie.insane.software"
app = Flask(__name__)

def call_device(state):
    url = f"{BASE_URL}/{EMAIL}/{PASSWORD}/{DEVICE_ID}/{state}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()

@app.route("/switch", methods=["POST"])
def switch():
    state = request.json.get("state")
    call_device(state)
    return jsonify({"ok": True})

@app.route("/health")
def health():
    return "ok"

app.run(host="0.0.0.0", port=8099)