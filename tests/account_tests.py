from tests.test_client import flask_app
from flask_tasks.viewmodels.accounts.register_view_model import RegisterViewModel
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

