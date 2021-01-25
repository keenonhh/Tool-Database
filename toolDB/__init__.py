from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key for use in wtforms
app.config['SECRET_KEY'] = '44680751eec5557106024cfaba4f817b'

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#import all the blueprints 
from toolDB.select_db.routes import select
from toolDB.insert_db.routes import insert

# register all the blueprints
app.register_blueprint(select)
app.register_blueprint(insert)

