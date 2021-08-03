from functools import wraps

import flask
from flask import current_app, Response
from flask import jsonify
from webargs.flaskparser import FlaskParser as BaseFlaskParser

from apifairy.exceptions import ValidationError


def _ensure_sync(f):
    if flask.__version__ < '2.' or hasattr(f, '_sync_ensured'):
        return f

    @wraps(f)
    def wrapper(*args, **kwargs):
        return current_app.ensure_sync(f)(*args, **kwargs)

    wrapper._sync_ensured = True
    return wrapper


def _annotate(f, **kwargs):
    if not hasattr(f, '_spec'):
        f._spec = {}
    for key, value in kwargs.items():
        f._spec[key] = value


def response(schema, status_code=200, description=None):
    if isinstance(schema, type):  # pragma: no cover
        schema = schema()

    def decorator(f):
        f = _ensure_sync(f)
        _annotate(f, response=schema, status_code=status_code,
                  description=description)

        @wraps(f)
        def _response(*args, **kwargs):
            rv = f(*args, **kwargs)
            if isinstance(rv, Response):  # pragma: no cover
                raise RuntimeError(
                    'The @response decorator cannot handle Response objects.')
            if isinstance(rv, tuple):
                json = schema.dump(rv[0])
                if len(rv) == 2:
                    if not isinstance(rv[1], int):
                        rv = (json, status_code, rv[1])
                    else:
                        rv = (json, rv[1])
                elif len(rv) >= 3:
                    rv = (json, rv[1], rv[2])
                else:
                    rv = (json, status_code)
                return rv
            else:
                return schema.dump(rv), status_code

        return _response

    return decorator
