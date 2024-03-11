from flask import Flask,render_template,request,url_for
from sqlite3 import Connection,connect,Cursor

app:Flask = Flask(__name__)


@app.route("/bestel",methods=["GET","POST"])
def bestel():
  if request.method == "POST":
    con:Connection = connect('database.db')
    cur:Cursor = Cursor(con)
    
    
    cur.executescript(f"""INSERT INTO bestellingen (
                      email,postcode,straatnaam,nummer) 
                      VALUES('{request.form.get("acountcode")}','{request.form.get("postcode")}',
                      '{request.form.get("straatnaam")}','{request.form.get("nummer")}')""")
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