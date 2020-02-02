import flask

from flask_tasks.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    return {}

@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    return {}

