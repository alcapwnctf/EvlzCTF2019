from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.recaptcha import RecaptchaField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')

class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField('Current Password',
                            validators=[DataRequired()])
    newpassword = PasswordField('New Password',
                            validators=[DataRequired()])
    newpasswordretype = PasswordField('Retype New Password',
                            validators=[DataRequired()])