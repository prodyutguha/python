from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    events = [
        {"title": "Saptami", "desc": "Morning rituals and evening aarti.", "image": "images/saptami.jpg"},
        {"title": "Ashtami", "desc": "Kumari Puja and Sandhi Puja celebrations.", "image": "images/ashtami.jpg"},
        {"title": "Navami", "desc": "Cultural programs and bhog distribution.", "image": "images/navami.jpg"},
        {"title": "Dashami", "desc": "Sindoor Khela & visarjan of Maa Durga.", "image": "images/dashami.jpg"},
    ]
    return render_template("index.html", events=events)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
