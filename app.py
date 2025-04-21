from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/api/salla/connect", methods=["POST"])
def connect_salla():
    data = request.get_json()
    client_id = data.get("client_id")
    client_secret = data.get("client_secret")

    token_url = "https://accounts.salla.sa/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "error": "فشل في جلب التوكن",
            "details": response.text
        }), 400

if __name__ == "__main__":
    print("✅ Flask app is starting...")
    app.run(port=5000, debug=True)
# تعديل جديد لاختبار رفع الملف إلى GitHub
