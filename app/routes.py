from flask.templating import render_template
from admin.routes import home
from run import app

@app.route('/')
def index():

    # --------------------------------------------------------------
    # Home
    # --------------------------------------------------------------
    from models import Home
    home = Home.query.all()

    # --------------------------------------------------------------
    # About
    # --------------------------------------------------------------
    from models import About
    about = About.query.all()

    # --------------------------------------------------------------
    # About -> Count
    # --------------------------------------------------------------
    from models import Count
    count = Count.query.all()

    # --------------------------------------------------------------
    # About -> TechnicalSkills
    # --------------------------------------------------------------
    from models import TechnicalSkills
    skills = TechnicalSkills.query.all()

    # --------------------------------------------------------------
    # About -> Education
    # --------------------------------------------------------------
    from models import Education
    education = Education.query.all()

    # --------------------------------------------------------------
    # About -> Interests
    # --------------------------------------------------------------
    from models import Interests
    interests = Interests.query.all()

    # --------------------------------------------------------------
    # About -> Testimonials
    # --------------------------------------------------------------
    from models import Testimonials
    testimonials = Testimonials.query.all()

    # --------------------------------------------------------------
    # PortFolio
    # --------------------------------------------------------------
    from models import Portfolio
    portfolio = Portfolio.query.all()

    # --------------------------------------------------------------
    # Blog
    # --------------------------------------------------------------
    from models import Blog
    blog = Blog.query.all()
    
    return render_template('app/index.html',about=about,testimonials=testimonials,portfolio=portfolio,home=home,count=count,skills=skills,education=education,interests=interests,blog=blog)
