from flask import Flask,render_template
from forms import Login,Registration

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == "__main__":
    app.run(debug=True)
from app import routes