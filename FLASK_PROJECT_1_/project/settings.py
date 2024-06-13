import flask

import homePage

project = flask.Flask(import_name = "settings")

project.register_blueprint(blueprint = homePage.home1)