from . import db
import app

class User(db.Model): # for creating new user
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    def __repr__(self):
        return f'User{self.username}' # function for debuging

class Role(db.Model):
     __tablename__ = 'roles'
     id = db.Column(db.Integer,primary_key = True)
     name = db.Column(db.String(255))
     users = db.relationship('User',backref = 'role',lazy="dynamic")# create a virtual column that will coonect with the foreign key



     def __repr__(self):
         return f'User{self.username}' # function for debuging



    