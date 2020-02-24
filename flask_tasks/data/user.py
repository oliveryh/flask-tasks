import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from flask_tasks.data.task import Task

from flask_tasks.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, unique=True, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now(), index=True)
    hashed_password = sa.Column(sa.String, nullable=True)

    tasks = orm.relation("Task", order_by=Task.created_date, back_populates="user")

    def __repr__(self):
        return "<User {}>".format(self.id)
