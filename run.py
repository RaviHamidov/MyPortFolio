from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = "static/assets/uploads"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587   
app.config['MAIL_USERNAME'] = "kharmacodingclub@gmail.com"
app.config['MAIL_PASSWORD'] = "math6734sfera09"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"

# db.session.commit()

migrate = Migrate(app, db)

from models import *

from app.routes import *

from admin.routes import *

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)  