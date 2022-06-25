from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class ReqForm(FlaskForm):
    location = StringField('Введите свой город')
    submit = SubmitField('Найти')