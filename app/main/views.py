from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user, login_user, logout_user
from ..models import User, Pitches, Comments
from .forms import CommentForm, PitchesForm, UpdateProfile
from .. import db,photos


@main.route('/')
def index():
    pitches = Pitches.query.all()
    comments = Comments.query.all()
    
    return render_template('index.html', pitches=pitches, comments=comments)




@main.route('/pitch/',methods=['GET','POST'])
@login_required
def pitches_form():
    pitches_form = PitchesForm()
    if pitches_form.validate_on_submit():
        title=pitches_form.title.data
        category=pitches_form.category.data
        pitch_content=pitches_form.pitch_content.data
        
        new_pitches = Pitches(title=title, pitch_content=pitch_content, category=category,user_id=current_user._get_current_object().id)
        new_pitches.save_pitches()
        return redirect(url_for('.index',))
    
    
    
    return render_template ('pitch.html', pitches_form=pitches_form)
        
        

@main.route('/comment/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    
    
    comment_form = CommentForm() 
    pitches=Pitches.query.get(pitch_id)
    comments= Comments.get_comments(pitch_id)
    user = User.query.filter_by(id=id)
    if comment_form.validate_on_submit():
        comments= comment_form.comment.data
        
        new_comment=Comments(pitch_id=pitch_id, comments=comments, user=user)
        new_comment.save_comments()
        
        return render_template('comment.html', comment_form=comment_form, pitches=pitches,user_id=current_user._get_current_object().id)



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




