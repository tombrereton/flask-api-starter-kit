from flask import Flask
# from flasgger import Swagger
from apifairy import APIFairy
from src.routes.home import home_api
from src.routes.users import users_api


def create_app():
    apifairy = APIFairy()
    app = Flask(__name__)

    # app.config['SWAGGER'] = {
    #     'title': 'Flask API Starter Kit',
    # }
    # swagger = Swagger(app)

    # Initialize Config
    app.config.from_object('src.config.DefaultConfig')

    apifairy.init_app(app)

    app.register_blueprint(home_api, url_prefix='/api')
    app.register_blueprint(users_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    print(app.url_map)

    app.run(host='0.0.0.0', port=port)
