import flask
from flask import request

from flask_tasks.infrastructure.view_modifiers import response
import flask_tasks.services.tasks_service as tasks_service
from flask_tasks.viewmodels.accounts.index_view_model import IndexViewModel

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    vm = IndexViewModel()

    if vm.user is None:
        return flask.redirect("/login")

    return vm.to_dict()


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
    vm = IndexViewModel()
    return vm.to_dict()
