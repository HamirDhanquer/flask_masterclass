from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship("Profile",backref="user", uselist=False)

    def __str__(self):
        return self.name

class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __str__(self):
        return self.photo

class Courses(db.Model):
    pass 


@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)