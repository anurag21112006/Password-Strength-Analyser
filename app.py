from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    strength = None
    score = 0
    color = ""
    suggestions = []

    if request.method == "POST":

        password = request.form["password"]

        if len(password) >= 8:
            score += 20
        else:
            suggestions.append("Increase password length")

        if any(c.isupper() for c in password):
            score += 20
        else:
            suggestions.append("Add uppercase letters")

        if any(c.islower() for c in password):
            score += 20
        else:
            suggestions.append("Add lowercase letters")

        if any(c.isdigit() for c in password):
            score += 20
        else:
            suggestions.append("Add numbers")

        if any(not c.isalnum() for c in password):
            score += 20
        else:
            suggestions.append("Add special characters")

        if score <= 40:
            strength = "Weak"
            color = "red"

        elif score <= 80:
            strength = "Medium"
            color = "orange"

        else:
            strength = "Strong"
            color = "green"

    return render_template(
        "index.html",
        strength=strength,
        score=score,
        color=color,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)