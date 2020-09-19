

from app.blueprints.base import new_blueprint


hello_blueprint = new_blueprint('hello', __name__)


@hello_blueprint.route('/open', methods=('POST', 'GET'))
def open_hello():
    return {
        'msg': 'open hello :)'
    }
