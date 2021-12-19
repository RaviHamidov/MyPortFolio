from flask_login.mixins import UserMixin
from admin.routes import contact
from run import db

class Home(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    home_icon_name=db.Column(db.String(100))
    home_icon_link=db.Column(db.String(100))

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

class Count(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    count_icon_name=db.Column(db.String(100))
    count_num=db.Column(db.String(100))
    count_title=db.Column(db.String(100))

class TechnicalSkills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skills_date=db.Column(db.String(100))
    skills_name=db.Column(db.String(100))
    skills_about=db.Column(db.String(100))

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_date=db.Column(db.String(100))
    education_name=db.Column(db.String(100))
    education_about=db.Column(db.String(100))

# Interests

class Interests(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    interests_icon_name=db.Column(db.String(100))
    education_title=db.Column(db.String(100))

# Testimonials

class Testimonials(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    testimonials_content=db.Column(db.String(100))
    testimonials_img=db.Column(db.String(100))
    testimonials_name=db.Column(db.String(100))
    testimonials_profession=db.Column(db.String(100))

# PortFolio

class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_icon=db.Column(db.String(100))
    portfolio_title=db.Column(db.String(100))
    portfolio_content=db.Column(db.String(100))

# Blog

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_icon_name=db.Column(db.String(100))
    blog_title_link=db.Column(db.String(100))
    blog_title_name=db.Column(db.String(100))
    blog_content=db.Column(db.String(100))

# Contact 

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_name = db.Column(db.String(50))
    contact_email = db.Column(db.String(100))
    contact_subject = db.Column(db.String(100))
    contact_message = db.Column(db.Text)

# Login

class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)
