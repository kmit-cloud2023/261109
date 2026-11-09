import random
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/randint", methods=["GET"])
def get_randint():
    return jsonify({"value": random.randint(0, 99)}), 200


@app.route("/api/rand", methods=["GET"])
def get_rand():
    return jsonify({"value": round(random.uniform(0, 99.9), 1)}), 200


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)