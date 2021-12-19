from flask_login.mixins import UserMixin
from run import db

class About(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_img=db.Column(db.String(100))
    about_title=db.Column(db.String(100))
    about_birthday=db.Column(db.String(100))
    about_website=db.Column(db.String(100))
    about_phone=db.Column(db.String(100))
    about_city=db.Column(db.String(100))
    about_age=db.Column(db.String(100))
    about_degree=db.Column(db.String(100))
    about_email=db.Column(db.String(100))
    about_freelance=db.Column(db.String(100))
    about_content=db.Column(db.Text())

class Testimonials(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    testimonials_content=db.Column(db.String(100))
    testimonials_img=db.Column(db.String(100))
    testimonials_name=db.Column(db.String(100))
    testimonials_profession=db.Column(db.String(100))

class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_icon=db.Column(db.String(100))
    portfolio_title=db.Column(db.String(100))
    portfolio_content=db.Column(db.String(100))

# Login
class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)