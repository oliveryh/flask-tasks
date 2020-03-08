import flask

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.viewmodels.accounts.index_view_model import IndexViewModel

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
def index():
    return flask.redirect("/task")


@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    vm = IndexViewModel()
    return vm.to_dict()
