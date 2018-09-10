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
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    users = db.relationship('User',backref = 'category',lazy="dynamic") 
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))

    def __repr__(self):
        return f'User {self.name}'  


class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    title = db.Column(db.String(255))
    date_of_pitch = db.Column(db.String(255))
    pitch_image = db.Column(db.String(255))
    content = db.Column(db.String(255))
    category = db.Column(db.String(255))
    category = db.relationship('Category',backref = 'pitch',lazy="dynamic")

