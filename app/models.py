from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    pitches = db.relationship('Pitch',backref = 'author',lazy="dynamic") 
    comments = db.relationship('Comment', backref = 'author', lazy = "dynamic")
    
    def save_user(self, user):
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username} {self.bio} {self.email}'


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    pitches = db.relationship('Pitch',backref = 'category',lazy="dynamic") 


    def save_category(self, category):
        db.session.add(category)
        db.session.commit()

    def __repr__(self):
        return f'{self.name}'  


class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    date_of_pitch = db.Column(db.String(255))
    content = db.Column(db.String(255))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    

    def save_pitch(self, pitch):
        db.session.add(pitch)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.title}'

class Comment(db.Model):
    __tablename__= 'comments'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String(255))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))

    
           

