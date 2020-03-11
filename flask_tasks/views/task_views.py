import flask

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.viewmodels.task.index_view_model import IndexViewModel
from flask_tasks.viewmodels.task.update_view_model import UpdateViewModel
from flask_tasks.viewmodels.task.create_view_model import CreateViewModel

blueprint = flask.Blueprint("task", __name__, template_folder="templates")



@blueprint.route("/task", methods=["GET"])
@response(template_file="task/index.html")
def task():
    vm = IndexViewModel()

    if vm.user is None:
        return flask.redirect("/login")

    vm.load_tasks()

    return vm.to_dict()

@blueprint.route("/task", methods=["POST"])
@response(template_file="task/index.html")
def task_create():
    vm = CreateViewModel()

    vm.validate()
    if vm.error:
        return flask.redirect("/task")

    vm.create()
    return flask.redirect("/task")

@blueprint.route("/task/update", methods=["POST"])
def task_update():
    vm = UpdateViewModel()
    vm.update()

    return {}
