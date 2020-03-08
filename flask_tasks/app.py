import os

import flask
import flask_tasks.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


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
