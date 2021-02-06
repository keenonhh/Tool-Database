from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key for use in wtforms
app.config['SECRET_KEY'] = '44680751eec5557106024cfaba4f817b'

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Khawk852!@localhost/Tool'
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