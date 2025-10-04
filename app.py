from flask import Flask, render_template, request, jsonify
import re
from checker.checker_generator import check_password_strength, generate_password

app = Flask(__name__)

def check_password(password):
    rules = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    score = sum(rules.values())
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    return {"rules": rules, "strength": strength}

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/checker")
def checker():
    return render_template("checker.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)

@app.route("/generator")
def generator():
    return render_template("generator.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 12))

    try:
        password = generate_password(length)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
