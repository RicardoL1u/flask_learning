from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello! this is the main page <h1>HELLO</h1>'

@app.route('/<name>') 
def user(name):
    return f'helo {name}'

@app.route('/admin')
def admin(): #
    # return redirect(url_for('home','admin')) # redict the admin page to home page
    return redirect(url_for("user", name="admin!")) # redirect to the user page


if __name__ == "__main__":
    app.run()