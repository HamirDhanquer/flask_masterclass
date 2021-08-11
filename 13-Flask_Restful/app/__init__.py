from config import config
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app( config_name ):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///flask_contacts.db"    
    #app.config["SECRET_KEY"] = "secret"
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api = Api(app, prefix="/api/v1")
    db.init_app(app)

    from app.resources.contacts import Contacts
    api.add_resource(Contacts, "/contacts")

    return app
