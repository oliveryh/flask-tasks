import flask
from flask import request

from flask_tasks.infrastructure.view_modifiers import response
from flask_tasks.infrastructure import request_dict
import flask_tasks.services.tasks_service as tasks_service
import flask_tasks.services.users_service as users_service
from infrastructure import cookie_auth

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    tasks = tasks_service.get_tasks()
    task_count = tasks_service.get_task_count()
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)
    if user_id is None:
        return flask.redirect("/login")

    user = users_service.get_user_by_id(user_id)
    if user is None:
        return flask.redirect("/login")

    return {
        "tasks": tasks,
        "task_count": task_count,
        "user": user,
        "user_id": cookie_auth.get_user_id_via_auth_cookie(flask.request),
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
    return {
        "user_id": cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }

@blueprint.route("/register", methods=["GET"])
@response(template_file="accounts/register.html")
def register_get():
    return {
        "user_id": cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }

@blueprint.route("/register", methods=["POST"])
@response(template_file="accounts/register.html")
def register_post():

    data = request_dict.create(default_val="")

    name = data.name
    email = data.email.lower().strip()
    password = data.password.strip()

    user = users_service.add_user(name, email, password)

    resp = flask.redirect("/")
    cookie_auth.set_auth(resp, user.id)

    return resp

@blueprint.route("/login", methods=["GET"])
@response(template_file="accounts/login.html")
def login_get():
    return {
        "user_id": cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }

@blueprint.route("/login", methods=["POST"])
@response(template_file="accounts/login.html")
def login_post():

    data = request_dict.create(default_val="")

    email = data.email.lower().strip()
    password = data.password.strip()

    user = users_service.login_user(email, password)

    if not user:
        return {
            "error": "The email or password you have entered is incorrect"
        }

    resp = flask.redirect("/")
    cookie_auth.set_auth(resp, user.id)

    return resp

@blueprint.route("/logout", methods=["GET"])
def logout_get():

    resp = flask.redirect("/")
    cookie_auth.logout(resp)
    return resp
