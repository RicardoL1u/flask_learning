from flask import Flask, redirect, url_for, render_template, request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'liuyantao'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column("name",db.String(20), unique=True)
    password = db.Column("password",db.String(50))
    email = db.Column("email", db.String(50), unique=True)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user",methods=["POST", "GET"])
def user():
    email = None
    if 'user' in session:
        user = session["user"]
        
        if request.method == "POST":
            email = request.form['email']
            session['email'] = email
        else:
            if "email" in session:
                email = session["email"]

        return f"<h1>{user}</h1>"

    else:
        return render_template(url_for('login.html'))

@app.route("/logout") 
def logout():
    session.pop("user", None)
    session.pop('email', None)
    flash('You were logged out','info')
    return redirect(url_for('login'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)