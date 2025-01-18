import sqlite3
from flask import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/apartments")
def apartments():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cards = cursor.execute("SELECT * FROM flat").fetchall()
    return render_template("apartments.html", cards=cards)

@app.route("/info/<p_type>/<int:p_id>")
def info(p_type, p_id):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cards = cursor.execute(f"SELECT * FROM '{p_type}' WHERE id LIKE '%{p_id}%'").fetchone()
    return render_template("info.html", product=cards)

@app.route("/houses")
def houses():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cards = cursor.execute("SELECT * FROM house").fetchall()
    return render_template("houses.html", cards=cards)


if __name__ == "__main__":
    app.run(debug=True)
