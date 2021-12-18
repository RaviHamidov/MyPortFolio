from flask.templating import render_template
from run import app

@app.route('/')
def app_index():
    from models import About
    about = About.query.all()
    return render_template('app/index.html',about=about)