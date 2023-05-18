from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from flask_login import current_user, login_required

from app import db
from app.Model.models import Student, Faculty, User
from app.Controller.forms import TAPositionForm, EditForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
@login_required
def index(role="ANY"):
    #posts = TAPositionForm.query.order_by(TAPositionForm.timestamp.desc())
    #return render_template('index.html', title="Smile Portal",  posts=posts.all())
    return render_template('index.html', title="Teaching Assistant App")

@bp_routes.route('/profile', methods=['GET'])
@login_required
def profile(role="ANY"):
    return render_template('profile.html', title="Display Profile", user = current_user)

@bp_routes.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def editprofile(role="ANY"):
    eform = EditForm()
    if request.method == 'POST':
        # handle the form submission
        if eform.validate_on_submit():
            current_user.firstname = eform.firstname.data
            current_user.lastname = eform.lastname.data
            current_user.wsuid = eform.wsuid.data
            current_user.email = eform.email.data
            current_user.address = eform.address.data
            current_user.phone = eform.phone.data
            current_user.set_password(eform.password.data)
            db.session.add(current_user)
            db.session.commit()
            flash("Your changes have been saved")
            return redirect(url_for('routes.display_profile'))
    elif request.method == 'GET':
        # populate the user data from DB
        eform.firstname.data = current_user.firstname
        eform.lastname.data = current_user.lastname
        eform.wsuid.data = current_user.wsuid
        eform.email.data = current_user.email
        eform.address.data = current_user.address
        eform.phone.data = current_user.phone     
    else:
        pass
    return render_template('edit_profile.html', title = 'Edit Profile', form = eform)
