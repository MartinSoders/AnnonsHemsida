''' Imports, two new compared to part 1 '''
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 
from user_info import user_info


''' ------------------ Set up app and database ----------------------------------------------- '''
# create the application object
app = Flask(__name__)
# Set database to AnnonsHemsida
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test_user:bananKALKON123!@localhost/AnnonsHemsida'
db = SQLAlchemy(app)



''' ------------------- Funktioner ---------------------------------------------------------- '''  

def Login(bool_value, username_string):
    global login_bool
    login_bool = bool_value
    
    global login_username
    login_username = username_string
    

## Login är en global funktion som ändras när inloggningen är godkänd
Login(False, "[username not definied]")  

''' ------------------ Routes / Sidor -------------------------------------------- '''


''' ________________REGISTER______________________ '''
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['submit button'] == 'Återgå':                   # Gå tillbax till login
            return redirect(url_for('login'))        
        if request.form['submit button'] == 'Registrera dig':           # Godkänn registrering
            
            # Ger en tom lista [] om användarnanet inte finns och en lista med en tuple [(uname_str, pass_str)] om namnet finns
            result = db.session.query(user_info).with_entities(user_info.username, user_info.password).filter(user_info.username.like(request.form['nuser'])).all()
            
            if result == []:                                                                                                              ### Skapar användare om användarnamnet inte finns        
                user_info.CreateUser(request.form['nuser'], request.form['npass'], request.form['nfirst'],
                                     request.form['nlast'], request.form['naddress'], request.form['npostal'],request.form['ncity'])
                return redirect(url_for('register_finished'))
                
            else:                                                                                                                           ### Ger varning om användarnamnet finns                                                                                                         
                return("Användarnamnet finns redan!")
            
    
    else:
        return render_template("register.html")
    

''' ________________REGISTER FINISHED______________ '''
@app.route('/register_finished', methods=['GET', 'POST'])
def register_finished():
    if request.method == 'POST':
        if request.form['submit button'] == 'Tillbaks till login':                   # Gå tillbax till login vid tryck på knappen
            return redirect(url_for('login'))    
    else:
        return render_template("register_finished.html")

''' _________________LOGIN______________________ '''
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        
        if request.form['submit button'] == 'Registrera':                                                                                                      # Om: Login-knappen
            return redirect(url_for('register'))
            
        
        if request.form['submit button'] == 'Login':                                                                                                           # Om: Login-knappen
            ## Användernamn och lösenord
            input_username = request.form['username']
            input_password = request.form['password']
        
            # Ger en tom lista [] om användarnanet inte finns och en lista med en tuple [(uname_str, pass_str)] om namnet finns
            result = db.session.query(user_info).with_entities(user_info.username, user_info.password).filter(user_info.username.like(input_username)).all()
        if result == []:                                                                                                                                       # Om inte använderen finns
            return f"Det finns ingen användare som heter {input_username}"
        else:
            if result[0][1] != request.form['password']:                                                                                                       # Om inte lösenordet stämmer
                return f"Felaktigt lösenord för användare {input_username}"
            else:                                                                                                                                              # Logga in och gå till home
                Login(True, input_username)  
                return redirect(url_for('home'))
        
    
    else:

        return render_template("login.html", error = error)




    


''' _________________HOME______________________ '''
@app.route('/home', methods=['GET', 'POST'])
def home():
    

    if not login_bool:                                                                                                                                          ## Om inte login_bool
        return "Var vänlig logga in"
    else:
        if request.method == 'POST':

            return f"Välkommen {login_username}"
        else:
            return render_template("home.html", 
                                   welcome_string = f"Välkommen {login_username}")
        


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)