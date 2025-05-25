from app import app
from app import render_template,Login,Registration
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    form = Registration()
    return render_template("registration.html",form=form)

@app.route("/login")
def login():
    form = Login()
    return render_template("Login.html",form=form)
