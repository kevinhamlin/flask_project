from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)


db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'danger'



mail = Mail(app)

from main.users.routes import users
from main.posts.routes import posts
from main.primary.routes import primary

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(primary)