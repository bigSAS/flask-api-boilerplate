from flask.blueprints import Blueprint


def new_blueprint(name: str, import_name: str):
    b = Blueprint(name, import_name)
    # todo: register generic err handler
    return b
