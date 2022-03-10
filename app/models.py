from turtle import title
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120), index=True, unique=True)  
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'pitcher',lazy = "dynamic")

    def save_user(self):
        db.session.add(self)
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
        return f'USER {self.username}'

class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    pitch_content = db.Column(db.String())
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id= db.Column(db.Integer, db.ForeignKey('categories_id'))
    comments = db.relationship("Comment", backref ='pitch', lazy = "dynamic")


    def save_pitches(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_pitches(cls,id):
            pitches = Pitches.query.filter_by(pitcher_id = id).order_by(Pitches.posted.desc())
            return pitches

    @classmethod
    def get_category_pitch(cls,id):
            category_pitches = Pitches.query.filter_by(category_id = id).order_by(Pitches.posted.desc())
            return category_pitches

    @classmethod
    def get_pitch_id(cls,id):
            pitch_id = Pitches.query.filter_by(id = id).order_by(Pitches.id.desc()) 
            return pitch_id


    def __repr__(self):
            return f"Pitches {self.title}"

    def __repr__(self):
        return f'User {self.name}'
    
    
class Categories(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key = True)
    categories_name = db.Column(db.String(255))
    pitches =db.relationship('Pitces', backref='category', lazy='dynamic')

    @classmethod
    def get_categories_name(cls, categories_name):
        category= Categories.query.filter_by(categories_name = categories_name).first()
        return category   
    
    def __repr__(self):
        return f'Categories {self.categories_name} '     


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Colum (db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(pitch_id=id).all()
        return comments


