class Config:
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///flask_contacts.db" 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug=True

class Testing(Config):
    pass


config  = {
    "development":Development
}