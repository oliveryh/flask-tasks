import flask_tasks.data.db_session as db_session
from flask_tasks.data.task import Task

def get_task_count() -> int:
    session = db_session.create_session()
    return session.query(Task).count()

def get_tasks() -> [Task]:
    session = db_session.create_session()
    return session.query(Task).all()