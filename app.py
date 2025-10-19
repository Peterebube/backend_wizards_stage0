from flask import Flask, jsonify
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/me", methods=["GET"])
def profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = response.json().get("fact", "Cats are mysterious animal")
    except requests.RequestException:
        cat_fact = "could not fetch cat fact at the moment."
    
    data = {
        "status": "success",
        "User": {
            "email": "Peterebubedike1@gmail.com",
            "name": "Peter Ebubedike",
            "stack": "Python--Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)