from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What would you like to pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('passionpitch','passionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('newspitch','newspitch')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

