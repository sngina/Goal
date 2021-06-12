from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# function of creating app.
def create_app(config_name):
    app = Flask(__name__)
    
    #Initializing flask extensions
    db.init_app(app)


    return app