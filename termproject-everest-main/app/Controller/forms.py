from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, PasswordField
from wtforms_sqlalchemy.fields import  QuerySelectMultipleField
from wtforms.validators import  DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from flask_login import current_user

from app.Model.models import User, Student, Faculty

class TAPositionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    #tag =  QuerySelectMultipleField( 'Tag', query_factory=get_tags , get_label=get_title, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
    body = TextAreaField('Body', validators=[DataRequired(), Length(min=0, max=1500)])
    submit = SubmitField('TAPositionForm')

class EditForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[Length(8)])  # we will have to check wether it is a valid or not
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = TextAreaField('Address', [Length(min=0, max = 200)])
    phone = TextAreaField('Address', [Length(10)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        students = Student.query.filter_by(email = email.data).all()
        for student in students:
            if (student.id != current_user.id):
                raise ValidationError('The email is already associated with another account! Please use a different email address.')

