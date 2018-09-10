from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required
from ..models import User 

app = Flask(__name__)

pitches = [{
    'author' : 'Yvonne Ojijo',
    'title' : 'political pitch',
    'pitchedOn' : 'Jun 17, 2018 13:46h',
    'image' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrT5Lov_-MXnTIvaiutU9bu9veV5s2ADSxOAV1bLaXTMp5KKF1FQ',
    'content' : 'Is the president rich???',
    'category' : 'political pitch'
},
{
    'author' : 'Diana Dee',
    'title' : 'Restorant launch',
    'pitchedOn' : 'Jan 23, 2018 21h',
    'image' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjBDuv8p-O1APxolflmsDkgjJjyfmCbELm4gruE1MLe4X6hzvQSQ',
    'content' : ' I am considering opening a high end Italian restaurant in downtown London because there are currently no such restaurants there. ',
    'category' : 'business pitch'
},
{
    'author' : 'Haron Lucky',
    'title' : 'Pitching my app on singing skills',
    'pitchedOn' : 'Sep 6, 2018 00:15h',
    'image' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShupA7GQRQvjBlQYvhiVbiWsF49LiODiqJ45wWVxbMrMA9aD0Q',
    'content' : 'I want to launch a Rocket',
    'category' : 'Political science'
},
{
    'author' : 'Maryanne Lenny',
    'title' : 'pitching on an inteview ',
    'pitchedOn' : 'Sep 6, 2018 12:30h',
    'image' : 'data:image/jpeg;base64,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',
    'content' : 'Why did you choose this course??',
    'category' : 'Interview pitch'
} 
]


# views
@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    title = 'Get started with a pitch'
    return render_template('index.html', title= title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

        return render_template("profile/profile.html", user = user)        


    
     