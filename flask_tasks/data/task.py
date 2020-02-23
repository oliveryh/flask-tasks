import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from flask_tasks.data.modelbase import SqlAlchemyBase

class Task(SqlAlchemyBase):
    __tablename__ = "tasks"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    due_date = sa.Column(sa.DateTime, nullable=True)
    desc = sa.Column(sa.String, nullable=True)
    completed = sa.Column(sa.Boolean, default=False)

    user_id = sa.Column(sa.String, sa.ForeignKey("users.id"))
    user = orm.relation("User")

    def __repr__(self):
        return "<Task {}>".format(self.id)