import os
import sys

import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import flask_tasks.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    configure()
    app.run(debug=True)

def configure():
    register_blueprints()
    setup_db()

def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), "db", "flasktask.sqlite")
    db_session.global_init(db_file)


def register_blueprints():
    from flask_tasks.views import home_views, account_views, task_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(task_views.blueprint)


if __name__ == "__main__":
    main()
else:
    configure()