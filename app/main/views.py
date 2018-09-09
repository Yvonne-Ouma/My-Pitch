from flask import render_template
from flask_login import login_required
from . import main

app = Flask(__name__)

@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    return render_template('index.html' title= title)

    
    
    

    
     