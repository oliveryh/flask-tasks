import flask

from flask_tasks.infrastructure.view_modifiers import response
import flask_tasks.services.tasks_service as tasks_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    task_count = tasks_service.get_task_count()
    return {
        "task_count": task_count
    }

@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    return {}

