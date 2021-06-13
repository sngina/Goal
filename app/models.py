from sqlalchemy.orm import backref , sessionmaker, relationship
from . import db
from werkzeug.security import generate_password_hash ,check_password_hash
from . import login_manager
from  flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin ,db.Model): # for creating new user
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User{self.username}' # function for debuging
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
class Category(db.Model):
    
    __tablename__ = 'category'

    # add columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    # saving category
    def save_category(self):
        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        
        categories = cls.query.all()
        return categories

#pitches
class Talk(db.Model):

    
    all_pitches = []

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    


    def save_pitch(self):
        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Talk.all_pitches.clear()

    # display pitches
    @classmethod
    def get_pitches(cls,id):
        pitches = Talk.query.order_by(Talk.date_posted.desc()).filter_by(category_id=id).all()
        return pitches


class Role(db.Model):
     __tablename__ = 'roles'
     id = db.Column(db.Integer,primary_key = True)
     name = db.Column(db.String(255))
     users = db.relationship('User',backref = 'role',lazy="dynamic")# create a virtual column that will connect with the foreign key



     def __repr__(self):
         return f'User{self.username}' # function for debuging

class Comments(db.Model):
    
    __tablename__ = 'comment'

    # add columns
    id = db.Column(db. Integer,primary_key = True)
    comment_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comment

    