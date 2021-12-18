from re import A
from werkzeug.utils import redirect
from run import app,db
# from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
# from run import login_manager
from flask import render_template,request,url_for
import os

@app.route("/admin/about",methods=["GET","POST"])
def blog():
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
def admin_about_delete(id):
        from models import About
        about=About.query.filter_by(id=id).first()
        db.session.delete(about)
        db.session.commit()
        return redirect('/admin/about')