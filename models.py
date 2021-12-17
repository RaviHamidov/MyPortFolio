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
    about_content=db.Column(db.String(200))
