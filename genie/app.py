from flask import Flask, request, jsonify
import requests
import os

BASE_URL = "https://genie.insane.software"

app = Flask(__name__)


def get_env():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    device_id = os.getenv("DEVICE_ID")

    if not email or not password or not device_id:
        raise ValueError("Missing EMAIL, PASSWORD, or DEVICE_ID")

    return email, password, device_id


def call_device(state: int):
    email, password, device_id = get_env()
    url = f"{BASE_URL}/{email}/{password}/{device_id}/{state}"

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


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "email_set": bool(os.getenv("EMAIL")),
        "password_set": bool(os.getenv("PASSWORD")),
        "device_id_set": bool(os.getenv("DEVICE_ID")),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8099)
