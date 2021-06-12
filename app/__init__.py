import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = flask(__name__)
    
    #Initializing flask extensions
    db.init_app(app)