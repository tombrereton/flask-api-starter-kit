import os

from dotenv import load_dotenv

load_dotenv()


class DefaultConfig(object):
    TESTING = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    FLASK_APP = os.getenv('FLASK_APP')
    DEFAULT_USERNAME = os.getenv('DEFAULT_USERNAME')
    APIFAIRY_UI = 'swagger_ui'
    APIFAIRY_UI_PATH = '/swagger'
    APIFAIRY_TITLE = 'Planning Crawler Api'
    APIFAIRY_APISPEC_PATH = '/apispec.json'
    APIFAIRY_VERSION = 1


class TestingConfig(DefaultConfig):
    TESTING = True
