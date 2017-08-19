from flask import Flask
from resources import blueprint as api
from config import DefaultConfig


# def create_app(config=None, app_name=None):
# if app_name is None:
#     app_name = DefaultConfig.PROJECT


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api/todo')
    app.run(debug=True)