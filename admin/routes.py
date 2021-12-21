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
        admin_username = "thehamidov",
        admin_password = "qizilmezun",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect (url_for("about"))

        else:
            return redirect(url_for("about"))

    return render_template("admin/login.html", login = login)

# --------------------------------------------------------------
# Logout 
# --------------------------------------------------------------

@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect('/')

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
        # mygmail = "kharmacodingclub@gmail.com"

        # msg = Message(contact_message, sender = contact_email, recipients = [mygmail])
        msg=Message(contact_subject, body=contact_message + " " + contact_email + " " + "tərəfindən göndərilmişdir" , sender=contact_email, recipients = ["kharmacodingclub@gmail.com"])

        mail.send(msg)

        db.session.add(cnt)
        db.session.commit()
        return redirect ("/admin/contact")
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
        return redirect("/admin/home")
        
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
        return redirect("/admin/about")
        
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
# About -> Count
# --------------------------------------------------------------

@app.route("/admin/count",methods=["GET","POST"])
@login_required
def count():
    from models import Count
    import os
    from run import db
    from werkzeug.utils import secure_filename
    count = Count.query.all()
    if request.method=="POST":
        count_icon_name = request.form["count_icon_name"]
        count_num = request.form["count_num"]

        cnt = Count(
            count_icon_name = count_icon_name,
            count_num = count_num
        )

        db.session.add(cnt)
        db.session.commit()
        return redirect("/admin/count")
        
    return render_template("admin/count.html", count=count)

@app.route("/admin/count/delete/<int:id>")
@login_required
def admin_count_delete(id):
        from models import Count
        portfolio=Count.query.filter_by(id=id).first()
        db.session.delete(count)
        db.session.commit()
        return redirect('/admin/count')


@app.route("/admin/count/edit/<int:id>",methods=["GET","POST"])
@login_required
def count_edit(id):
    from models import Count
    from run import db
    newCount = Count.query.filter_by(id=id).first()
    if request.method=="POST":
        count = Count.query.filter_by(id=id).first()
        count.count_icon_name = request.form["count_icon_name"]
        count.count_num = request.form["count_num"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_count.html", newCount=newCount)

# --------------------------------------------------------------
# About -> TechnicalSkills
# --------------------------------------------------------------

@app.route("/admin/technicalskills",methods=["GET","POST"])
@login_required
def technicalskills():
    from models import TechnicalSkills
    import os
    from run import db
    from werkzeug.utils import secure_filename
    technicalskills = TechnicalSkills.query.all()
    if request.method=="POST":
        skills_date = request.form["skills_date"]
        skills_name = request.form["skills_name"]
        skills_about = request.form["skills_about"]

        tchskl = TechnicalSkills(
            skills_date = skills_date,
            skills_name = skills_name,
            skills_about = skills_about
        )

        db.session.add(tchskl)
        db.session.commit()
        return redirect("/admin/technicalskills")
        
    return render_template("admin/technicalskills.html", technicalskills=technicalskills)

@app.route("/admin/technicalskills/delete/<int:id>")
@login_required
def admin_technicalskills_delete(id):
        from models import TechnicalSkills
        technicalskills=TechnicalSkills.query.filter_by(id=id).first()
        db.session.delete(technicalskills)
        db.session.commit(technicalskills)
        return redirect('/admin/technicalskills')


@app.route("/admin/technicalskills/edit/<int:id>",methods=["GET","POST"])
@login_required
def technicalskills_edit(id):
    from models import TechnicalSkills
    from run import db
    newTechnicalSkills = TechnicalSkills.query.filter_by(id=id).first()
    if request.method=="POST":
        technicalskills = TechnicalSkills.query.filter_by(id=id).first()
        technicalskills.skills_date = request.form["skills_date"]
        technicalskills.skills_name = request.form["skills_name"]
        technicalskills.skills_about = request.form["skills_about"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_technicalskills.html", newTechnicalSkills=newTechnicalSkills)

# --------------------------------------------------------------
# About -> Education
# --------------------------------------------------------------

@app.route("/admin/education",methods=["GET","POST"])
@login_required
def education():
    from models import Education
    import os
    from run import db
    from werkzeug.utils import secure_filename
    education = Education.query.all()
    if request.method=="POST":
        education_date = request.form["education_date"]
        education_name = request.form["education_name"]
        education_about = request.form["education_about"]

        edc = Education(
            education_date = education_date,
            education_name = education_name,
            education_about = education_about
        )

        db.session.add(edc)
        db.session.commit()
        return redirect("/admin/education")
        
    return render_template("admin/education.html", education=education)

@app.route("/admin/education/delete/<int:id>")
@login_required
def admin_education_delete(id):
        from models import Education
        education=Education.query.filter_by(id=id).first()
        db.session.delete(education)
        db.session.commit(education)
        return redirect('/admin/education')


@app.route("/admin/education/edit/<int:id>",methods=["GET","POST"])
@login_required
def education_edit(id):
    from models import Education
    from run import db
    newEducation = Education.query.filter_by(id=id).first()
    if request.method=="POST":
        education = Education.query.filter_by(id=id).first()
        education.skills_date = request.form["skills_date"]
        education.skills_name = request.form["skills_name"]
        education.skills_about = request.form["skills_about"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_education.html", newEducation=newEducation)

# --------------------------------------------------------------
# About -> Interests
# --------------------------------------------------------------

@app.route("/admin/interests",methods=["GET","POST"])
@login_required
def interests():
    from models import Interests
    import os
    from run import db
    from werkzeug.utils import secure_filename
    interests = Interests.query.all()
    if request.method=="POST":
        interests_date = request.form["interests_date"]
        interests_name = request.form["interests_name"]
        interests_about = request.form["interests_about"]

        int = Interests(
            interests_date = interests_date,
            interests_name = interests_name,
            interests_about = interests_about
        )

        db.session.add(int)
        db.session.commit()
        return redirect("/admin/interests")
        
    return render_template("admin/interests.html", interests=interests)

@app.route("/admin/interests/delete/<int:id>")
@login_required
def admin_interests_delete(id):
        from models import Interests
        interests=Interests.query.filter_by(id=id).first()
        db.session.delete(interests)
        db.session.commit(interests)
        return redirect('/admin/interests')


@app.route("/admin/interests/edit/<int:id>",methods=["GET","POST"])
@login_required
def interests_edit(id):
    from models import Interests
    from run import db
    newInterests = Interests.query.filter_by(id=id).first()
    if request.method=="POST":
        interests = Interests.query.filter_by(id=id).first()
        interests.interests_date = request.form["interests_date"]
        interests.interests_name = request.form["interests_name"]
        interests.interests_about = request.form["interests_about"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_interests.html", newInterests=newInterests)

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
        return redirect("/admin/testimonials")
        
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
        return redirect("/admin/portfolio")
        
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

# --------------------------------------------------------------
# Blog
# --------------------------------------------------------------

@app.route("/admin/blog",methods=["GET","POST"])
@login_required
def blog():
    from models import Blog
    import os
    from run import db
    from werkzeug.utils import secure_filename
    blog = Blog.query.all()
    if request.method=="POST":
        blog_icon_name = request.form["blog_icon_name"]
        blog_title_link = request.form["blog_title_link"]
        blog_title_name = request.form["blog_title_name"]
        blog_content = request.form["blog_content"]

        blg = Blog(
            blog_icon_name = blog_icon_name,
            blog_title_link = blog_title_link,
            blog_title_name = blog_title_name,
            blog_content = blog_content
        )

        db.session.add(blg)
        db.session.commit()
        return redirect("/admin/blog")
        
    return render_template("admin/blog.html", blog=blog)

@app.route("/admin/blog/delete/<int:id>")
@login_required
def admin_blog_delete(id):
        from models import Blog
        blog=Blog.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit()
        return redirect('/admin/blog')


@app.route("/admin/blog/edit/<int:id>",methods=["GET","POST"])
@login_required
def blog_edit(id):
    from models import Blog
    from run import db
    newBlog = Blog.query.filter_by(id=id).first()
    if request.method=="POST":
        blog = Blog.query.filter_by(id=id).first()
        blog.blog_icon_name = request.form["blog_icon_name"]
        blog.blog_title_link = request.form["blog_title_link"]
        blog.blog_title_name = request.form["blog_title_name"]
        blog.blog_content = request.form["blog_content"]
        db.session.commit()
        return redirect("/")
    return render_template("/admin/update_blog.html", newBlog=newBlog)