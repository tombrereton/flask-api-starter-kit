"""[General Configuration Params]
"""
import os

from dotenv import load_dotenv


load_dotenv()


class DefaultConfig(object):
    TESTING = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    FLASK_APP = os.getenv('FLASK_APP')
    DEFAULT_USERNAME = os.getenv('DEFAULT_USERNAME')
    APIFAIRY_UI = 'swagger_ui'


class TestingConfig(DefaultConfig):
    TESTING = True
