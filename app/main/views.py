from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required
from ..models import User,Pitch,Category

app = Flask(__name__)


# views
@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    title = 'Get started with a pitch'
    pitches = Pitch.query.all()

    return render_template('index.html', title= title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

        return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        
    return redirect(url_for('main.profile',uname=uname))            


    
     