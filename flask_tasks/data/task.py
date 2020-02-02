import sqlalchemy as sa

from flask_tasks.data.modelbase import SqlAlchemyBase

class Task(SqlAlchemyBase):
    __tablename__ = "tasks"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime)
    due_date = sa.Column(sa.DateTime)
    desc = sa.Column(sa.String)
    complete = sa.Column(sa.Boolean)
    owner = sa.Column(sa.String)

    def __repr__(self):
        return "<Task {}>".format(self.id)