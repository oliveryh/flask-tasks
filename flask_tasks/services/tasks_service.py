from flask import jsonify

import flask_tasks.data.db_session as db_session
from flask_tasks.data.task import Task
from flask_tasks.data.user import User


def get_user_task_count(user_id) -> int:
    session = db_session.create_session()
    return len(session.query(User).filter(User.id == user_id).first().tasks)


def get_user_tasks(user_id) -> [Task]:
    session = db_session.create_session()
    return session.query(User).filter(User.id == user_id).first().tasks


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
