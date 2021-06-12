from . import db
import app
from werkzeug.security import generate_password_hash ,check_password_hash
from . import login_manager
from . import views,forms

class User(db.Model): # for creating new user
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
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}' # function for debuging
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Role(db.Model):
     __tablename__ = 'roles'
     id = db.Column(db.Integer,primary_key = True)
     name = db.Column(db.String(255))
     users = db.relationship('User',backref = 'role',lazy="dynamic")# create a virtual column that will coonect with the foreign key



     def __repr__(self):
         return f'User{self.username}' # function for debuging



    