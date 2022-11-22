## Från denna: https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates


''' Imports, two new compared to part 1 '''
from flask import Flask, render_template, redirect, url_for, request, current_app, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from user import user_info

# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test_user:bananKALKON123!@localhost/AnnonsHemsida'
db = SQLAlchemy(app)

## Class UserInfo

class Annons(db.Model):
    id = db.Column(db.Integer, unique = True, autoincrement = True, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    username = db.Column(db.String(80), db.ForeignKey("user_info.username"), nullable=False)
    start_dt = db.Column(db.DateTime, nullable=False)
    stop_dt = db.Column(db.DateTime, nullable=False)
    start_price = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Integer, nullable=True)
    
  
class AnnonsHistory(db.Model):
     Annons_id = db.Column(db.Integer, db.ForeignKey("Annons.id"), nullable = False)
     username = db.Column(db.String(80), db.ForeignKey("user_info.username"), nullable=False)
     bid_nr = db.Column(db.Integer, unique = True, autoincrement = True, primary_key=True)
     bid_price = db.Column(db.Integer, unique = True, autoincrement = True, primary_key=True)
     
     
    
 




### För att testa HOME 
@app.route('/home_test', methods=['GET', 'POST'])
def home():
    
    ## Dummy, ska vara global
    login_username = "Martin Testar"
    
    
    alla_annonser = Annons.query
    
    
                                                                                                                                          
    if request.method == 'POST':
        return f"Välkommen {login_username}"
    else:
        return render_template("home_test.html", 
                                welcome_string = f"Välkommen {login_username}")
        


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)