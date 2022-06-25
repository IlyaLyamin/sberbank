import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, name='name')
    surname = sqlalchemy.Column(sqlalchemy.String, name='surname')
    email = sqlalchemy.Column(sqlalchemy.String, name='email')
    age = sqlalchemy.Column(sqlalchemy.Integer, name='age')
    reit = sqlalchemy.Column(sqlalchemy.Float, name='reit')
    location = sqlalchemy.Column(sqlalchemy.String, name='location')