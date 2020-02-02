import flask
from infrastructure.view_modifiers import response

app = flask.Flask(__name__)


@app.route("/")
@response(template_file="home/index.html")
def index():
    return {}


if __name__ == "__main__":
    app.run(debug=True)
