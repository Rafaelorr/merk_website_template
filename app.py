from flask import Flask,render_template,request,url_for
import sqlite3
from random import randint

app:Flask = Flask(__name__)


@app.route("/bestel",methods=["GET","POST"])
def bestel():
  if request.method == "POST":
    bestelling:dict = {
      "acountcode":request.form.get("acountcode"),
      "postcode":request.form.get("postcode"),
      "straatnaam":request.form.get("straatnaam"),
      "nummer":request.form.get("nummer")
    }
    con:sqlite3.Connection = sqlite3.connect('database.db')
    cur:sqlite3.Cursor = sqlite3.Cursor(con)
    
    
    cur.executescript('INSERT INTO bestellingen (email,postcode,straatnaam,nummer) VALUES('+ bestelling["acountcode"] +','+bestelling["postcode"]+','+bestelling["straatnaam"]+','+bestelling["nummer"]+')')
    con.commit()

    cur.close()
    con.close()
    return render_template("succes.html")
  return render_template("bestel.html",bestel=url_for("bestel"))

@app.route("/")
def home():
  return render_template("home.html",bestel_link=url_for("bestel"))

@app.route("/create_acount",methods=["GET","POST"])
def create_acount():
  if request.method == "POST":
    con:sqlite3.Connection = sqlite3.connect('database.db')
    cur:sqlite3.Cursor = sqlite3.Cursor(con)
    while True:
      for _ in range(10000000):
        acountcode = randint(1,9999999)
        print(acountcode)
        cur.execute("FROM acountcodes SELECT *")
        acounts = cur.fetchall()
        print(acounts)
        if acountcode in acounts:
          continue
        else:
          break
      if acountcode not in acounts:
        break
      else:
        return "er zijn acountcodes meer over"
    cur.executescript('INSERT INTO acountcodes (acountcodes,credits) VALUES('+acountcode+',50)')
    return render_template("create_acount_succes.html",acountcode=acountcode)
  return render_template('create_acount.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)