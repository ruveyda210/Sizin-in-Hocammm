from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/mesaj")
def mesaj():
    return render_template("mesaj.html")

if __name__ == "__main__":
    app.run(debug=True)