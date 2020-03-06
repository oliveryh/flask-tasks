# noinspection PyPackageRequirements
import pytest

import sys
import os

container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)

import flask_tasks.app
from flask_tasks.app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()

    # noinspection PyBroadException,PyUnusedLocal
    try:
        flask_tasks.app.register_blueprints()
    except Exception as x:
        # print(x)
        pass

    flask_tasks.app.setup_db()

    yield client
