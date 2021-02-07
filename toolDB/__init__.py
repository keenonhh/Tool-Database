from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# secret key for use in wtforms
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#import all the blueprints 
from toolDB.select_db.routes import select
from toolDB.insert_db.routes import insert
from toolDB.delete_db.routes import delete
from toolDB.update_db.routes import update

# register all the blueprints
app.register_blueprint(select)
app.register_blueprint(insert)
app.register_blueprint(delete)
app.register_blueprint(update)