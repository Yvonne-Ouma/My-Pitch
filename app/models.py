from .import db 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(255))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    users = db.relationship('User',backref = 'category',lazy="dynamic") 

    def __repr__(self):
        return f'User {self.name}'       