from flask_tasks.viewmodels.task.create_view_model import CreateViewModel
from tests.test_client import flask_app

def test_vm_empty_task_throughs_error():
    # Arrange
    form_data = {
        "desc": "   "
    }

    with flask_app.test_request_context(path="/task/create", data=form_data):
        vm = CreateViewModel()

    vm.validate()

    assert vm.error is not None

