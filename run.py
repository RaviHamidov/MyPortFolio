from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db=SQLAlchemy(app)

# db.session.commit()

migrate = Migrate(app, db)

from models import *

from app.routes import *

from admin.routes import *

if __name__=='__main__':
    # db.create_all()
    app.run(debug=True)  