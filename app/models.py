from turtle import title
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120), index=True, unique=True)  
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
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

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    pitch_content = db.Column(db.String())
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id= db.Column(db.Integer, db.ForeignKey('categories_id'))
    comments = db.relationship("Comment", backref ='pitch', lazy = "dynamic")


    def save_pitch(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_user_pitch(cls,id):
            user_pitches = Pitch.query.filter_by(pitcher_id = id).order_by(Pitch.posted.desc())
            return user_pitches

    @classmethod
    def get_category_pitch(cls,id):
            category_pitches = Pitch.query.filter_by(category_id = id).order_by(Pitch.posted.desc())
            return category_pitches

    @classmethod
    def get_pitch_id(cls,id):
            pitch_id = Pitch.query.filter_by(id = id).order_by(Pitch.id.desc()) 
            return pitch_id


    def __repr__(self):
            return f"Pitch {self.title}"

    def __repr__(self):
        return f'User {self.name}'
    
    
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()

@classmethod
def get_reviews(cls,id):
    reviews = Review.query.filter_by(movie_id=id).all()
    return reviews

@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
    self.pass_secure = generate_password_hash(password)


def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))