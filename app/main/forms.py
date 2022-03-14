from random import choices
from tkinter.tix import InputOnly, Select
from tokenize import String
from turtle import title
from unicodedata import category
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
class PitchesForm(FlaskForm):
    title= StringField('Title:', validators=[InputRequired()])
    category= SelectField('Category', choices= [('Make a choice','Make a choice'), ('Lifestyle','Lifestyle'), ('Business', 'Business'), ('Technology', 'Technology')], validators=[InputRequired()])
    pitch_content=TextAreaField('Share your field', validators=[InputRequired()])
    submit= SubmitField('Submit')
    
    
class CommentForm(FlaskForm):
    comment=TextAreaField('Comment', validators=[InputRequired()])
    submit=SubmitField('Submit')
    