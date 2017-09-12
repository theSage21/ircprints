import flask


application = flask.Flask()


@application.route('/', methods=['GET'])
def home():
    return "home"
