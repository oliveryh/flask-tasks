from flask import jsonify

import flask_tasks.data.db_session as db_session
from flask_tasks.data.task import Task


def get_task_count() -> int:
    session = db_session.create_session()
    return session.query(Task).count()


def get_tasks() -> [Task]:
    session = db_session.create_session()
    return session.query(Task).all()


def item_completed(task_id) -> dict:
    session = db_session.create_session()
    task = session.query(Task).get(task_id)
    if task is None:
        return jsonify({"status": "Failed"})
    task.completed = True
    session.commit()


def item_uncompleted(task_id) -> dict:
    session = db_session.create_session()
    task = session.query(Task).get(task_id)
    if task is None:
        return jsonify({"status": "Failed"})
    task.completed = False
    session.commit()
