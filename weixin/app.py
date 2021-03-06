# -*- coding: utf-8 -*-

import os

from flask import Flask

from weixin.config import config
from weixin.extensions import oauth
from weixin.extensions import sentry
from weixin.views import bp


def configure_app(app):
    config_name = os.getenv('WEIXIN_ENV') or 'default'
    app.config.from_object(config[config_name])


def register_extensions(app):
    oauth.init_app(app)
    sentry.init_app(app)


def register_blueprints(app):
    app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)
    configure_app(app)
    register_extensions(app)
    register_blueprints(app)
    return app
