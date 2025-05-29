from app import app
from app import render_template,Login,Registration
from flask_login import current_user, login_user,logout_user
from flask import redirect,url_for,flash
from app.database import User,db
from sqlalchemy import select
from flask import request
from urllib.parse import urlsplit
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    form = Registration()
    return render_template("registration.html",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = db.session.scalar(select(User).where(User.login == form.username.data))
        
        if user is None or not user.check_password(form.password.data):
            flash("Не верный логин или пароль")
            return redirect(url_for("login"))
        login_user(user,form.remember_me.data) 
        next_page = request.args.get("next")
        if not next_page or  urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("Login.html",form=form)

@app.route("/log_out")
def log_out():
    logout_user()
    return redirect(url_for("index"))
