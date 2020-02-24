import flask
from flask import request

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.infrastructure import request_dict
import flask_tasks.services.tasks_service as tasks_service
import flask_tasks.services.users_service as users_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    tasks = tasks_service.get_tasks()
    task_count = tasks_service.get_task_count()
    return {
        "task_count": task_count,
        "tasks": tasks
    }

@blueprint.route("/update_task", methods=["POST"])
def update_task():
    data = request.json
    task_id = data["id"]
    if data["type"] == "item_completed":
        tasks_service.item_completed(task_id)
    elif data["type"] == "item_uncompleted":
        tasks_service.item_uncompleted(task_id)
    return {}

@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    return {}

@blueprint.route("/register", methods=["GET"])
@response(template_file="home/register.html")
def register_get():
    return {}

@blueprint.route("/register", methods=["POST"])
@response(template_file="home/register.html")
def register_post():

    data = request_dict.create(default_val="")

    name = data.name
    email = data.email.lower().strip()
    password = data.password.strip()

    user = users_service.add_user(name, email, password)

    resp = flask.redirect("/")

    return resp

