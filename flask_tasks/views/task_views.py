import flask

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.viewmodels.task.index_view_model import IndexViewModel
from flask_tasks.viewmodels.task.update_view_model import UpdateViewModel

blueprint = flask.Blueprint("task", __name__, template_folder="templates")


@blueprint.route("/task")
@response(template_file="task/index.html")
def task():
    vm = IndexViewModel()

    if vm.user is None:
        return flask.redirect("/login")

    return vm.to_dict()


@blueprint.route("/task/update", methods=["POST"])
def task_update():
    vm = UpdateViewModel()
    vm.update()

    return {}
