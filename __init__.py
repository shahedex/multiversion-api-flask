import os

from flask import Flask


# application factory funcion
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='HELLO_FROM_THE_FLASK',
        DATABASE=os.path.join(app.instance_path, 'multiversion-api-flask.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple route that says hello
    @app.route('/hello')
    def hello():
        return 'Hello from the core API!'

    return app