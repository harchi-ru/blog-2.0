from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    username = StringField("Login",validators=[DataRequired("Поле не может быть пустым")])
    password = PasswordField("Password",validators=[DataRequired("Поле не может быть пустым")])

class Login(Form):
    submit = SubmitField("Авторизироваться")
    
class Registration(Form):
    submit = SubmitField("Зарегистрироваться")