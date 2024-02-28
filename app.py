from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bestel")
def bestel():
    if request.method == "POST":
        pass
    render_template()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)