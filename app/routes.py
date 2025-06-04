from app import app
from app import render_template,Login,Registration
from flask_login import current_user, login_user,logout_user,login_required
from flask import redirect,url_for,flash
from app.database import User,db
import sqlalchemy as sa
from flask import request
from urllib.parse import urlsplit
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User(login = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Поздравляю вы зарегистрированы")
        return redirect(url_for("login"))
    else:
        print(form.errors)
        
    return render_template("registration.html", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.login == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Не верный логин или пароль")
            return redirect(url_for("login"))
        login_user(user,form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html",form=form)



@app.route("/log_out")
def log_out():
    logout_user()
    return redirect(url_for("index"))

@app.route("/profile/<username>")
@login_required
def profile(username):
    user = db.first_or_404(sa.select(User).where(User.login == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template("profile.html", user=user, posts=posts)
