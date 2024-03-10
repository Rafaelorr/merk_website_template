from flask import Flask,render_template,request,url_for
import sqlite3

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
    
    
    cur.executescript(f"""INSERT INTO bestellingen (
                      email,postcode,straatnaam,nummer) 
                      VALUES('{bestelling["acountcode"]}','{bestelling["postcode"]}',
                      '{bestelling["straatnaam"]}','{bestelling["nummer"]}')""")
    con.commit()

    cur.close()
    con.close()
    return render_template("succes.html")
  return render_template("bestel.html",bestel=url_for("bestel"))

@app.route("/")
def home():
  return render_template("home.html",bestel_link=url_for("bestel"))


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)