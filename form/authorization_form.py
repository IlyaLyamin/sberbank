from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AuthorizationForm(FlaskForm):
    email_f = StringField('Почта', validators=[DataRequired()])
    id_f = StringField('Id', validators=[DataRequired()])
    submit = SubmitField('Войти')