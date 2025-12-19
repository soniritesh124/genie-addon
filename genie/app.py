from flask import Flask, request, jsonify
import requests
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
DEVICE_ID = os.getenv("DEVICE_ID")

BASE_URL = "https://genie.insane.software"
app = Flask(__name__)

def call_device(state):
    if not EMAIL or not PASSWORD or not DEVICE_ID:
        raise ValueError("Missing EMAIL, PASSWORD, or DEVICE_ID environment variables")

    url = f"{BASE_URL}/{EMAIL}/{PASSWORD}/{DEVICE_ID}/{state}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()

@app.route("/switch", methods=["POST"])
def switch():
    if not request.is_json:
        return jsonify({"error": "JSON body required"}), 400

    data = request.get_json()
    state = data.get("state")

    if state not in (0, 1):
        return jsonify({"error": "state must be 0 or 1"}), 400

    try:
        call_device(state)
        return jsonify({"ok": True, "state": state})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "email_set": bool(EMAIL),
        "password_set": bool(PASSWORD),
        "device_id_set": bool(DEVICE_ID)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8099)
