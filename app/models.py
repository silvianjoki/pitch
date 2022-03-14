
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# from datetime import datetime

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
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comments', backref='author', lazy='dynamic')
    pitches = db.relationship('Pitches',backref = 'pitcher',lazy = "dynamic")

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
    category = db.Column(db.String())
    pitch_content = db.Column(db.String())
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comments", backref ='pitch', lazy = "dynamic")
    
    def save_pitches(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_pitches(cls,category):
            pitches = Pitches.query.filter_by(category=category).all()
            return pitches



class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column (db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # posted = db.Column(db.DateTime,default=datetime.utcnow)
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comments.query.filter_by(pitch_id=pitch_id).all()
        return comments
    




