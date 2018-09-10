from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required
from ..models import User 

app = Flask(__name__)

@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    title = 'Get started with a pitch'
    return render_template('index.html', title= title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)


    return render_template("profile/profile.html", user = user)        


    
    

    
     