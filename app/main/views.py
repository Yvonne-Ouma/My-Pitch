from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required
from ..models import User 

app = Flask(__name__)

pitch = [{
    'author' : 'Yvonne Ojijo',
    'title' : 'My rocket launch',
    'postedOn' : 'Jun 16, 2018 18:24h',
    'image' : 'https://www.google.com/imgres?imgurl=http%3A%2F%2Fcoloredfaces.com%2Fimg%2Favatars%2FrJM6HQsLT6bGC8i.png&imgrefurl=http%3A%2F%2Fcoloredfaces.com%2Fen%2Fcolors%2F13990c&docid=n0sFT9B8wHWLDM&tbnid=4Hqzk9H9gY4CmM%3A&vet=10ahUKEwjtnKaVyq_dAhVmLMAKHRiBCE4QMwjGAigwMDA..i&w=960&h=960&client=ubuntu&bih=602&biw=1366&q=avatar%20for%20profile&ved=0ahUKEwjtnKaVyq_dAhVmLMAKHRiBCE4QMwjGAigwMDA&iact=mrc&uact=8',
    'content' : 'Is the president rich???',
    'category' : 'political pitch'
},
{
    'author' : 'Diana Dee',
    'title' : 'Pitching my app on recipes',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'image' : 'http://cdn03.cdn.justjared.com/wp-content/uploads/headlines/2018/08/zhavia-deep.jpg',
    'content' : 'I want to launch a Rocket',
    'category' : 'Interview Pitch'
},
{
    'author' : 'Jason Derulo',
    'title' : 'Pitching my app on singing skills',
    'postedOn' : 'Sep 6, 2018 00:15h',
    'image' : 'https://i.pinimg.com/474x/94/93/a9/9493a949cf32ff3424e80603d823eb0b--avatar-created-by.jpg',
    'content' : 'I want to launch a Rocket',
    'category' : 'Political science'
},
{
    'author' : 'Jouqin Chen',
    'title' : 'Pitching my app on ',
    'postedOn' : 'Sep 6, 2018 00:15h',
    'image' : 'https://ubistatic19-a.akamaihd.net/ubicomstatic/nn-NO/global/custom-module/Camila_Cabello-Havana_331839.jpg',
    'content' : 'I want to launch a Rocket',
    'category' : 'Business'
} 
]


# views
@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    title = 'Get started with a pitch'
    return render_template('index.html', title= title, pitch= pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)


    return render_template("profile/profile.html", user = user)        


    
    

    
     