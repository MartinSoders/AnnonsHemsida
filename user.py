''' Imports, two new compared to part 1 '''
from flask import Flask, render_template, redirect, url_for, request, current_app, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test_user:bananKALKON123!@localhost/AnnonsHemsida'
db = SQLAlchemy(app)

## Class UserInfo

class user_info(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key = True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    postal_code = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    
    def CreateUser(uname, upass, ufirst, ulast, uaddress, upostal, ucity):
        
            
        u = user_info()
        u.username = uname
        u.password = upass
        u.firstname = ufirst
        u.lastname = ulast
        u.address = uaddress
        u.postal_code = str(upostal) ## Gör string om input blir int
        u.city = ucity
        with app.app_context():
            db.session.add(u)
            db.session.commit()
            
        
## Class UserInfo

class user_login(db.Model):

    # Tid och ID fixas automatiskt
    login_id = db.Column(db.Integer, unique = True, autoincrement = True, primary_key=True)
    login_time = db.Column(db.DateTime, default=datetime.now)
    user_name = db.Column(db.String(80), db.ForeignKey("user_info.username"), nullable=False)
    user_ip = db.Column(db.String(80), nullable = False)
    def Register(user_name, user_ip):
        l = user_login()
        l.user_name = user_name
        l.user_ip = user_ip
        
        
              
        ## Registrerar inloggningen 
        with app.app_context():
            db.session.add(l)
            db.session.commit()


             
    
with app.app_context():
    db.create_all()


    
    
