from flask.templating import render_template
from run import app

@app.route('/')
def index():

    from models import About
    about = About.query.all()

    from models import Testimonials
    testimonials = Testimonials.query.all()

    from models import Portfolio
    portfolio = Portfolio.query.all()
    
    return render_template('app/index.html',about=about,testimonials=testimonials,portfolio=portfolio)
