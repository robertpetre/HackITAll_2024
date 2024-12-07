#!/usr/bin/env python3

from app import app
from werkzeug.serving import run_simple 


if __name__ == '__main__':
    run_simple(
        hostname="0.0.0.0",
        application=app,
        port=5000,
        use_reloader=True,
        use_debugger=True,
        threaded=True
    )