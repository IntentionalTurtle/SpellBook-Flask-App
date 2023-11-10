from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

#set variables for class instantiation

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default='')
    last_name = db.Column(db.String(150), nullable = True, default='')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

#defaults need to go towards the end...so email should go first as it can't have a default
#__init__ to save user values
    def __init__(self, email, first_name = '', last_name = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
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
    
class Spell(db.Model):
    id = db.Column(db.String, primary_key = True)
    url = db.Column(db.String(300), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    level = db.Column(db.String(2))
    casting_time = db.Column(db.String(25))
    duration = db.Column(db.String(50))
    classes = db.Column(db.String(100))
    desc = db.Column(db.String)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, id, url, name, level, casting_time, duration, classes, desc, user_token):
        self.id = id
        self.url = url
        self.name = name
        self.level = level
        self.casting_time = casting_time
        self.duration = duration
        self.classes = classes
        self.desc = desc
        self.user_token = user_token

    def __repr__(self):
        return f'The following spell has been added to mybook: {self.name}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class SpellSchema(ma.Schema):
    class Meta:
        fields = ['id', 'url','name','level','casting_time','duration', 'classes', 'desc', 'user_token']

spell_schema = SpellSchema()
spells_schema = SpellSchema(many = True)

class Feature(db.Model):
    id = db.Column(db.String, primary_key = True)
    url = db.Column(db.String(300), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    level = db.Column(db.String(2))
    classes = db.Column(db.String(100))
    desc = db.Column(db.String)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, id, url, name, level, casting_time, duration, classes, desc, user_token):
        self.id = id
        self.url = url
        self.name = name
        self.level = level
        self.classes = classes
        self.desc = desc
        self.user_token = user_token

    def __repr__(self):
        return f'The following feature has been added to mybook: {self.name}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class FeatureSchema(ma.Schema):
    class Meta:
        fields = ['id', 'url','name','level', 'classes', 'desc', 'user_token']

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many = True)