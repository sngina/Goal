from ..import auth
from app.auth.forms import LoginForm
from flask import render_template,request,redirect,url_for,abort
from . import main 
from ..models import  User ,Category ,Talk ,Comments
from flask_login import login_required , current_user
from .. import db 
from . forms import PepForm, CommentForm
from app.main import forms
import markdown2

# Views

@main.route('/')
def index():

   
    categories = Category.get_categories()
    
    title = 'Home - Welcome to One Minute Pitch'
    return render_template('index.html', title = title ,categories = categories)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    else:
        pitches = Talk.query.filter_by(user_id = current_user.id).all()
        return render_template("profile/profile.html", user = user ,pitches = pitches)
 #function  ya category
@main.route('/category/<int:id>', methods = ['GET','POST'])
def category(id):
    pitches = Category.get_categories(id)
    
    # pitches = Category.query.get(id)
    print(category)
    if category is None:
        abort(404)

    pitches = Talk.get_pitches(id)
    title = "Pitches"
    return render_template('category.html', title = title,category=category,pitches = pitches)

# Dynamic routing for pitches
@main.route('/pitches', methods = ['GET','POST'])
@login_required
def pitches():
    

    
    form = PepForm()
    pitche = pitches.query.filter_by(id=id).first()

    if category is None:
       abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch = PepForm(content=content,user_id=current_user.id,category_id=category.id ,description = category.description)
        new_pitch.save_pitch()
        return redirect(url_for('category',content = content,))

    title = 'Pitches'
    return render_template('new_pitch.html', title = title, pitch_form = form)


@main.route('/single_pitch', methods = ['GET','POST'])
@login_required
def single_pitch():
    
    # pitches = talk.query.get(id)

    if pitches is None:
        abort(404)

    form = PepForm()

    if form.validate_on_submit():
        single_pitchtalk= single_pitch.get_single_pitch(id)
        title = 'Comment Section'
        return render_template('pitch.html', title = title, pitches = pitches, comment = comment)

# fuction ya comment

@main.route('/comment/<id>', methods = ['GET','POST'])
@login_required
def comment(id):
    
    form = CommentForm()
    comment=Comments.query.filter_by(id=id).first()

    # if pitches is None:
    #     abort(404)

    if form.validate_on_submit():
        comment_section_id = form.comment_section_id.data
        comment = CommentForm(comment_section_id=comment_section_id,user_id=current_user.id,pitches_id=pitches.id)
        comment.save_comment()
        return redirect(url_for('.category', id = pitches.id))

    title = 'Comment'
    return render_template('comments.html', title = title, comment_form = form)