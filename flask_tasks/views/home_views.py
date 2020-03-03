import flask
from flask import request

from flask_tasks.infrastructure.view_modifiers import response
import flask_tasks.services.tasks_service as tasks_service
from infrastructure import cookie_auth
from flask_tasks.viewmodels.accounts.index_view_model import IndexViewModel
from flask_tasks.viewmodels.accounts.login_view_model import LoginViewModel
from flask_tasks.viewmodels.accounts.register_view_model import RegisterViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    vm = IndexViewModel()
    if vm.user_id is None:
        return flask.redirect("/login")

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


@blueprint.route("/register", methods=["GET"])
@response(template_file="accounts/register.html")
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route("/register", methods=["POST"])
@response(template_file="accounts/register.html")
def register_post():
    vm = RegisterViewModel()

    vm.validate()

    if vm.error:
        return vm.to_dict()

    vm.register_user()

    resp = flask.redirect("/")
    cookie_auth.set_auth(resp, vm.user.id)

    return resp


@blueprint.route("/login", methods=["GET"])
@response(template_file="accounts/login.html")
def login_get():
    vm = LoginViewModel()
    return vm.to_dict()


@blueprint.route("/login", methods=["POST"])
@response(template_file="accounts/login.html")
def login_post():
    vm = LoginViewModel()

    vm.validate()

    if vm.error:
        return vm.to_dict()

    resp = flask.redirect("/")
    cookie_auth.set_auth(resp, vm.user.id)

    return resp


@blueprint.route("/logout", methods=["GET"])
def logout_get():
    resp = flask.redirect("/")
    cookie_auth.logout(resp)
    return resp
