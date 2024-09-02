from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default='', unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been added to the database'

# ========================================================================
class Employee(db.Model):
    id = db.Column(db.String, primary_key=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    Position = db.Column(db.String(150))
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(100))
    Address = db.Column(db.String(150))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, FirstName, LastName, Position, Phone, Email, Address, City_ST_Zip, user_token, id=''):
        self.id = self.set_id()
        self.FirstName = FirstName
        self.LastName = LastName
        self.Position = Position
        self.Phone = Phone
        self.Email = Email
        self.Address = Address
        self.City_ST_Zip = City_ST_Zip
        self.user_token = user_token

    def __repr__(self):
        return f'The following Employee has been added to the directory: {self.FirstName} {self.LastName}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'FirstName', 'LastName', 'Position', 'Phone', 'Email', 'Address','City_ST_Zip']
                  
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
    
# =========================================================================
class Student(db.Model):
    id = db.Column(db.String, primary_key=True)
    FirstName = db.Column(db.String(200), nullable=False)
    LastName = db.Column(db.String(200), nullable=False)
    Photo = db.Column(db.String(200))
    Parent1 = db.Column(db.String(200), nullable=False)
    Parent2 = db.Column(db.String(200))
    Phone1 = db.Column(db.String(200), nullable=False)
    Phone2 = db.Column(db.String(200))
    Email1 = db.Column(db.String(200))
    Email2 = db.Column(db.String(200))
    Address1 = db.Column(db.String(200))
    Address2 = db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, FirstName, LastName, Photo, Parent1, Parent2, Phone1, Phone2, Email1, Email2, Address1, Address2, user_token, id=''):
        self.id = self.set_id()
        self.FirstName = FirstName
        self.LastName = LastName
        self.Photo = Photo
        self.Parent1 = Parent1
        self.Parent2 = Parent2
        self.Phone1 = Phone1
        self.Phone2 = Phone2
        self.Email1 = Email1
        self.Email2 = Email2
        self.Address1 = Address1
        self.Address2 = Address2
        self.user_token = user_token

    def __repr__(self):
        return f'The following Student has been added to the directory: {self.FirstName} {self.LastName}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class StudentSchema(ma.Schema):
    class Meta:
        fields = ['id', 'FirstName', 'LastName', 'Photo', 'Parent1', 'Parent2', 'Phone1', 'Phone2', 'Email1','Email2', 'Address1', 'Address2' ]
                  
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
