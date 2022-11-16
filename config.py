import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "esta-es-una-clave-secreta"
    SQLALCHEMY_DATABASE_URI = "mysql://root:nethack@localhost/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
