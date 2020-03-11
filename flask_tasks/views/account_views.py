import flask

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.infrastructure import cookie_auth
from flask_tasks.viewmodels.accounts.login_view_model import LoginViewModel
from flask_tasks.viewmodels.accounts.register_view_model import RegisterViewModel

blueprint = flask.Blueprint("account", __name__, template_folder="templates")


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
