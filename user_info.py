''' Imports, two new compared to part 1 '''
from flask import Flask, render_template, redirect, url_for, request, current_app
from flask_sqlalchemy import SQLAlchemy

# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test_user:bananKALKON123!@localhost/AnnonsHemsida'
db = SQLAlchemy(app)

## Class UserInfo

class user_info(db.Model):
    def __init__(self):
        pass
    
    id = db.Column(db.Integer, unique = True, autoincrement = True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
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
            
        
    
    
with app.app_context():
    db.create_all()
    #user_info.CreateUser("admin", "admin", "admin", "adminsson", "admingatan 1", "1337", "admin city")