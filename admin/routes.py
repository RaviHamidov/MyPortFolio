from re import A
from werkzeug.utils import redirect
from run import app,db
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager
from flask import render_template,request,url_for
import os

# --------------------------------------------------------------
# Login
# --------------------------------------------------------------

@login_manager.user_loader
def load_user(user_id):
    from models import Login
    return Login.query.get(int(user_id))

@app.route("/admin",methods=["GET","POST"])
def admin_login():
    from models import Login
    from run import db
    login = Login(
        admin_username = "admin",
        admin_password = "admin",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect (url_for("about"))

        else:
            return redirect(url_for("admin_login"))

    return render_template("admin/login.html", login = login)

# --------------------------------------------------------------
# Logout 
# --------------------------------------------------------------

@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect (url_for("about"))

# --------------------------------------------------------------
# Contact
# --------------------------------------------------------------

@app.route("/admin/contact", methods=["GET","POST"])
@login_required
def contact():
    from models import Contact
    from run import db
    import smtplib
    from flask_mail import Mail, Message
    from run import mail
    messages = Contact.query.all()
    if request.method == "POST":
        contact_name = request.form["contact_name"]
        contact_email = request.form["contact_email"]
        contact_subject = request.form["contact_subject"]
        contact_message = request.form["contact_message"]
        cnt = Contact(
            contact_name = contact_name,
            contact_email = contact_email,
            contact_subject = contact_subject,
            contact_message = contact_message
        )
        msg = cnt.contact_message  
        mygmail = "kharmacodingclub@gmail.com"

        msg = Message(contact_message, sender = contact_email, recipients = [mygmail])
        mail.send(msg)

        db.session.add(cnt)
        db.session.commit()
        return redirect ("/")
    return render_template("admin/contact.html", messages=messages)

@app.route("/admin/contact/delete/<int:id>")
@login_required
def admin_contact_delete(id):
        from models import Contact
        messages=Contact.query.filter_by(id=id).first()
        db.session.delete(messages)
        db.session.commit()
        return redirect('/admin/contact')

# --------------------------------------------------------------
# Home
# --------------------------------------------------------------

@app.route("/admin/home",methods=["GET","POST"])
@login_required
def home():
    from models import Home
    import os
    from run import db
    from werkzeug.utils import secure_filename
    home = Home.query.all()
    if request.method=="POST":
        home_icon_name = request.form["home_icon_name"]
        home_icon_link = request.form["home_icon_link"]

        hom = Home(
            home_icon_name = home_icon_name,
            home_icon_link = home_icon_link
        )

        db.session.add(hom)
        db.session.commit()
        return redirect("/")
        
    return render_template("admin/home.html", home=home)

@app.route("/admin/home/delete/<int:id>")
@login_required
def admin_home_delete(id):
        from models import Home
        portfolio=Home.query.filter_by(id=id).first()
        db.session.delete(home)
        db.session.commit()
        return redirect('/admin/home')


@app.route("/admin/home/edit/<int:id>",methods=["GET","POST"])
@login_required
def home_edit(id):
    from models import Home
    from run import db
    newHome = Home.query.filter_by(id=id).first()
    if request.method=="POST":
        home = Home.query.filter_by(id=id).first()
        home.home_icon_name = request.form["home_icon_name"]
        home.home_icon_link = request.form["home_icon_link"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_home.html", newHome=newHome)

# --------------------------------------------------------------
# About
# --------------------------------------------------------------

@app.route("/admin/about",methods=["GET","POST"])
@login_required
def about():
    from models import About
    import os
    from run import db
    from werkzeug.utils import secure_filename
    about = About.query.all()
    if request.method=="POST":
        file = request.files['about_img']
        filename=file.filename
        file.save(os.path.join('static/assets/uploads/',filename))
        about_title = request.form["about_title"]
        about_birthday = request.form["about_birthday"]
        about_website = request.form["about_website"]
        about_phone = request.form["about_phone"]
        about_city = request.form["about_city"]
        about_age = request.form["about_age"]
        about_degree = request.form["about_degree"]
        about_email = request.form["about_email"]
        about_freelance = request.form["about_freelance"]
        about_content = request.form["about_content"]

        abt = About(
            about_img = filename,
            about_title = about_title,
            about_birthday = about_birthday,
            about_website = about_website,
            about_phone = about_phone,
            about_city = about_city,
            about_age = about_age,
            about_degree = about_degree,
            about_email = about_email,
            about_freelance = about_freelance,
            about_content = about_content
        )

        db.session.add(abt)
        db.session.commit()
        return redirect("/")
        
    return render_template("admin/about.html", about=about)

@app.route("/admin/about/delete/<int:id>")
@login_required
def admin_about_delete(id):
        from models import About
        about=About.query.filter_by(id=id).first()
        db.session.delete(about)
        db.session.commit()
        return redirect('/admin/about')


@app.route("/admin/about/edit/<int:id>",methods=["GET","POST"])
@login_required
def about_edit(id):
    from models import About
    from run import db
    newAbout = About.query.filter_by(id=id).first()
    if request.method=="POST":
        about = About.query.filter_by(id=id).first()
        about.about_title = request.form["about_title"]
        about.about_birthday = request.form["about_birthday"]
        about.about_website = request.form["about_website"]
        about.about_phone = request.form["about_phone"]
        about.about_city = request.form["about_city"]
        about.about_age = request.form["about_age"]
        about.about_degree = request.form["about_degree"]
        about.about_email = request.form["about_email"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_about.html", newAbout=newAbout)

# --------------------------------------------------------------
# Testimonials
# --------------------------------------------------------------

@app.route("/admin/testimonials",methods=["GET","POST"])
@login_required
def testimonials():
    from models import Testimonials
    import os
    from run import db
    from werkzeug.utils import secure_filename
    testimonials = Testimonials.query.all()
    if request.method=="POST":
        testimonials_content = request.form["testimonials_content"]
        file = request.files["testimonials_img"]
        filename=file.filename
        file.save(os.path.join('static/assets/uploads/',filename))
        testimonials_name = request.form["testimonials_name"]
        testimonials_profession = request.form["testimonials_profession"]

        tst = Testimonials(
            testimonials_content = testimonials_content,
            testimonials_img = filename,
            testimonials_name = testimonials_name,
            testimonials_profession = testimonials_profession
        )

        db.session.add(tst)
        db.session.commit()
        return redirect("/")
        
    return render_template("admin/testimonials.html", testimonials=testimonials)

@app.route("/admin/testimonials/delete/<int:id>")
@login_required
def admin_testimonials_delete(id):
        from models import Testimonials
        testimonials=Testimonials.query.filter_by(id=id).first()
        db.session.delete(testimonials)
        db.session.commit()
        return redirect('/admin/testimonials')


@app.route("/admin/testimonials/edit/<int:id>",methods=["GET","POST"])
@login_required
def testimonials_edit(id):
    from models import Testimonials
    from run import db
    newTestimonials = Testimonials.query.filter_by(id=id).first()
    if request.method=="POST":
        testimonials = Testimonials.query.filter_by(id=id).first()
        testimonials.testimonials_content = request.form["testimonials_content"]
        testimonials.testimonials_name = request.form["testimonials_name"]
        testimonials.testimonials_profession = request.form["testimonials_profession"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_testimonials.html", newTestimonials=newTestimonials)


# --------------------------------------------------------------
# Portfolio
# --------------------------------------------------------------

@app.route("/admin/portfolio",methods=["GET","POST"])
@login_required
def portfolio():
    from models import Portfolio
    import os
    from run import db
    from werkzeug.utils import secure_filename
    portfolio = Portfolio.query.all()
    if request.method=="POST":
        portfolio_icon = request.form["portfolio_icon"]
        portfolio_title = request.form["portfolio_title"]
        portfolio_content = request.form["portfolio_content"]

        prt = Portfolio(
            portfolio_icon = portfolio_icon,
            portfolio_title = portfolio_title,
            portfolio_content = portfolio_content
        )

        db.session.add(prt)
        db.session.commit()
        return redirect("/")
        
    return render_template("admin/portfolio.html", portfolio=portfolio)

@app.route("/admin/portfolio/delete/<int:id>")
@login_required
def admin_portfolio_delete(id):
        from models import Portfolio
        portfolio=Portfolio.query.filter_by(id=id).first()
        db.session.delete(portfolio)
        db.session.commit()
        return redirect('/admin/portfolio')


@app.route("/admin/portfolio/edit/<int:id>",methods=["GET","POST"])
@login_required
def portfolio_edit(id):
    from models import Portfolio
    from run import db
    newPortfolio = Portfolio.query.filter_by(id=id).first()
    if request.method=="POST":
        portfolio = Portfolio.query.filter_by(id=id).first()
        portfolio.portfolio_icon = request.form["portfolio_icon"]
        portfolio.portfolio_title = request.form["portfolio_title"]
        portfolio.portfolio_content = request.form["portfolio_content"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_portfolio.html", newPortfolio=newPortfolio)