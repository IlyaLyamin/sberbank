import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Question(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'question'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    question = sqlalchemy.Column(sqlalchemy.String)
    options = sqlalchemy.Column(sqlalchemy.String)
    correct_option_id = sqlalchemy.Column(sqlalchemy.String)
    explanation = sqlalchemy.Column(sqlalchemy.String)
