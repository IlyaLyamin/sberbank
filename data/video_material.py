import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class VideoMaterial(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'video'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    url = sqlalchemy.Column(sqlalchemy.String, name='video')
    material = sqlalchemy.Column(sqlalchemy.String, name='material')
    lvl = sqlalchemy.Column(sqlalchemy.Integer, name='lvl')