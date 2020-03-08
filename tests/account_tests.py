import os
import sys

from flask import Response

container_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(container_folder)
sys.path.insert(0, container_folder)


from flask_tasks.data.user import User
from flask_tasks.data.task import Task
from flask_tasks.viewmodels.accounts.register_view_model import RegisterViewModel
from flask_tasks.views.account_views import register_post
from tests.test_client import flask_app, client
import unittest.mock


def test_register_validation_for_existing_user():
    # Arrange
    form_data = {
        "name": "Oliver",
        "email": "oo@oo.oo",
        "password": "o" * 6,
    }

    with flask_app.test_request_context(path="/register", data=form_data):
        vm = RegisterViewModel()

    # Act
    target = "flask_tasks.services.users_service.does_email_exist"
    with unittest.mock.patch(target, return_value=True):
        vm.validate()

    # Assert
    assert vm.error is not None
    assert "email already exists" in vm.error


def test_register_validation_when_valid():
    # Arrange
    form_data = {
        "name": "Oliver",
        "email": "oo@oo.oo",
        "password": "o" * 6,
    }

    with flask_app.test_request_context(path="/register", data=form_data):
        vm = RegisterViewModel()

    # Act
    target = "flask_tasks.services.users_service.does_email_exist"
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    # Assert
    assert vm.error is None


def test_register_view_new_user():
    # Arrange
    form_data = {
        "name": "Oliver",
        "email": "oo@oo.oo",
        "password": "o" * 6,
    }

    # Act
    does_email_exist = "flask_tasks.services.users_service.does_email_exist"
    email_not_taken = unittest.mock.patch(does_email_exist, return_value=None)
    add_user = "flask_tasks.services.users_service.add_user"
    user_returned = unittest.mock.patch(add_user, return_value=User())
    register_context = flask_app.test_request_context(path="/register", data=form_data)
    with email_not_taken, user_returned, register_context:
        resp: Response = register_post()

    # Assert
    assert resp.location == "/"


def test_int_account_home_with_login(client):
    get_user_by_id = "flask_tasks.services.users_service.get_user_by_id"
    test_user = User(name="Michael", email="michael@talkpython.fm")
    get_tasks = "flask_tasks.services.tasks_service.get_tasks"
    test_tasks = [
        Task(desc="Task 1"),
        Task(desc="Task 2"),
    ]
    get_task_count = "flask_tasks.services.tasks_service.get_task_count"
    test_task_count = 2

    user = unittest.mock.patch(get_user_by_id, return_value=test_user)
    tasks = unittest.mock.patch(get_tasks, return_value=test_tasks)
    task_count = unittest.mock.patch(get_task_count, return_value=test_task_count)
    with user, tasks, task_count:
        resp: Response = client.get("/")

    assert resp.status_code == 200
    assert b"Michael" in resp.data
