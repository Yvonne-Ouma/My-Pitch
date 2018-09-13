from flask import Flask
from . import main
from flask import render_template,redirect, request, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import User,Pitch,Comment
from .forms import MinutePitchForm,UpdateProfile,CommentForm
from .. import db, photos


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

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)        

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


    
@main.route('/pitch/new', methods=['GET', 'POST'])  
@login_required
def new_pitch():
    form= MinutePitchForm()

    if form.validate_on_submit():
        title = form.title.data 
        content = form.content.data 
        category = form.category.data 

        pitch = Pitch(title = title,content = content, category = category)

        db.session.add(pitch)
        db.session.commit()

        print('yvonne')
        flash('Creating pitch has been successful!')
        return redirect(url_for('main.one_pitch', id = pitch.id))


    return render_template('newP.html', title='New Pitch',pitch_form = form, legend = 'New Pitch')

@main.route('/pitch/new/<int:id>')
def one_pitch(id):
    pitch = Pitch.query.get(id)
    return render_template('onePitch.html', pitch = pitch)



@main.route('/pitch/<int:pitch_id>/',methods = ["GET","POST"])
def pitch(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    form = CommentForm()

    if form.validate_on_submit():
        title = form.title.data 
        comment = form.comment.data 
        new_pitch_comment = Comment(title = title,
                                    comment=comment,
                                    pitch_id = pitch_id)

        db.session.add(new_pitch_comment) 
        db.session.commit()

    comments = Comment.query.all()
    return render_template('comment_pitch.html', title = pitch.title, pitch =pitch, pitch_form = form, comments = comments) 






        
