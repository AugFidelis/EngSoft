from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_bd_aula.sqlite3"

db = SQLAlchemy(app)

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(50), nullable = False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/')
def index():
    return render_template('index.html',usuarios = usuario.query.all())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # user = usuario(username = request.form["Augusto"], email = request.form["augusto@hotmail.com"])
        # db.session.add(user)
        # db.session.commit()
    app.run(debug=True)