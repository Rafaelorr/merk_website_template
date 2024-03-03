from flask import Flask,render_template,request,url_for
import sqlite3

app:Flask = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/bestel",methods=["GET","POST"])
def bestel():
  if request.method == "POST":
      bestelling:dict = {
          "email":request.form.get("email"),
          "postcode":request.form.get("postcode"),
          "straatnaam":request.form.get("straatnaam"),
          "nummer":request.form.get("nummer")
      }
      con:sqlite3.Connection = sqlite3.connect('database.db')
      cur:sqlite3.Cursor = sqlite3.Cursor(con)

      cur.executescript('INSERT INTO bestellingen (email,postcode,straatnaam,nummer) VALUES('+ bestelling["email"] +','+bestelling["postcode"]+','+bestelling["straatnaam"]+','+bestelling["nummer"]+')')
      con.commit()

      cur.close()
      con.close()
      render_template("succes.html")
  render_template("bestel.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)