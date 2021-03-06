import unittest.mock

from flask import Response

from flask_tasks.data.user import User
from flask_tasks.data.task import Task
from flask_tasks.viewmodels.accounts.register_view_model import RegisterViewModel
from flask_tasks.views.account_views import register_post
from tests.test_client import flask_app, client


def test_vm_register_user_exists():
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


def test_vm_register_user_doesnt_exist():
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


def test_v_register_successful_redirects_to_home():
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
    get_user_tasks = "flask_tasks.services.tasks_service.get_user_tasks"
    test_tasks = [
        Task(desc="Task 1"),
        Task(desc="Task 2"),
    ]
    get_user_task_count = "flask_tasks.services.tasks_service.get_user_task_count"
    test_task_count = 2

    user = unittest.mock.patch(get_user_by_id, return_value=test_user)
    tasks = unittest.mock.patch(get_user_tasks, return_value=test_tasks)
    task_count = unittest.mock.patch(get_user_task_count, return_value=test_task_count)
    with user, tasks, task_count:
        resp: Response = client.get("/task")

    assert resp.status_code == 200
    assert b"Michael" in resp.data
