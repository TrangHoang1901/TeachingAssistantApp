from datetime import datetime
from app import db
from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import declarative_base
from app import login

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     happiness_level = db.Column(db.Integer, default = 3)


class User(db.Model):  # db.Base
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(64),  index=True)
    firstname =  db.Column(db.String(100))
    lastname =  db.Column(db.String(100))
    wsuid =  db.Column(db.Integer, unique=True, index = True)
    email = db.Column(db.String(120), unique=True, index=True)
    address =  db.Column(db.String(200))
    phone =  db.Column(db.Integer)
    user_role = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))

    __mapper_args__ = {
        'polymorphic_identity': 'user_table',
        'polymorphic_on': user_role
    }

    def __init__(self,username,firstname,lastname,wsuid,email,address,phone,user_role):
            self.username = username
            self.firstname = firstname
            self.lastname = lastname
            self.wsuid = wsuid
            self.email = email
            self.address = address
            self.phone = phone
            self.user_role = user_role

    def __repr__(self):
        return 'ID: {} User Name: {}'.format(self.id, self.username)
    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_user_role(self):
        return self.user_role

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    #representative_name = db.Column(db.String(45), default = 2)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    } 
    
class Faculty(User):
    __tablename__ = 'staff_account'
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    #representative_name = db.Column(db.String(45))

    __mapper_args__ = {
        'polymorphic_identity': 'faculty'
    } 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))   