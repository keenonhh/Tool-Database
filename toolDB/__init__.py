from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# secret key for use in wtforms
#app.config['SECRET_KEY'] = '44680751eec5557106024cfaba4f817b'

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#from workoutapp.users.routes import users
#from workoutapp.home.routes import home
#from workoutapp.workouts.routes import workouts
#
# register all the blueprints
#app.register_blueprint(users)
#app.register_blueprint(home)
#app.register_blueprint(workouts)


## Configure db
#db = yaml.load(open('db.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']
#
#mysql = MySQL(app)
#
#@app.route('/', methods=['GET', 'POST'])
#def index():
#    if request.method == 'POST':
#        # Fetch form data
#        userDetails = request.form
#        name = userDetails['name']
#        email = userDetails['email']
#        cur = mysql.connection.cursor()
#        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
#        mysql.connection.commit()
#        cur.close()
#        return redirect('/users')
#    return render_template('index.html')
#
#@app.route('/users')
#def users():
#    cur = mysql.connection.cursor()
#    resultValue = cur.execute("SELECT * FROM users")
#    if resultValue > 0:
#        userDetails = cur.fetchall()
#        return render_template('users.html',userDetails=userDetails)
#
