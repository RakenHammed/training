#!/usr/bin/env bash
set -e

if [ "$ENV" = "production" ]; then
    exec gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'
else
    exec flask run
fi