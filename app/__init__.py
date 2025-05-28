from flask import Flask,render_template
from app.forms import Login,Registration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import dotenv_values

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

config = dotenv_values(".flaskenv")


if __name__ == "__main__":
    app.run(config["FLASK_DEBUG"])
from app import routes,database