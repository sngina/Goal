from sqlalchemy.orm import query
from ..import auth
from app.auth.forms import LoginForm
from flask import render_template,request,redirect,url_for,abort
from . import main 
from ..models import  User ,Pitch ,User ,Comment, Upvote, Downvote
from flask_login import login_required ,current_user
from .. import db 
from. forms import PitchForm, CommentForm,UpvoteForm,Downvote
from app.main import forms
import markdown2

# Views

@main.route('/', methods = ['GET' , 'POST'])
def index():

 
    pname = Pitch.query.filter_by().first()
    title = 'Home'
    passionpitch= Pitch.query.filter_by(category="passionpitch")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    newspitch = Pitch.query.filter_by(category = "newspitch")
    productpitch = Pitch.query.filter_by(category = "productpitch")
    upvotes = Upvote.query.filter_by()
    downvote = Downvote.query.filter_by()

    return render_template('home.html', title = title, passionpitch=passionpitch, interviewpitch= interviewpitch, productpitch = productpitch, newspitch = newspitch, upvotes=upvotes)
    




@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)




@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch )



@main.route('/pitch/likes/<pitch_id>' , methods =  ['GET' ,'POST'])  
@login_required	
def upvote(pitch_id):
    if Upvote.query.filter(Upvote.user_id==current_user.id , Upvote.pitch_id==pitch_id).first():
        return redirect(url_for('main.index'))
    new_upvotes = Upvote(pitch_id=pitch_id,user_id= current_user)
    new_upvotes.save_upvotes()
    return redirect (url_for('main.index'))

  
   