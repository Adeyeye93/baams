#!/usr/bin/env bash
# exit on error
set -o errexit

# Install pipenv if not already installed
pip install pipenv

pipenv install --deploy --ignore-pipfile

python manage.py collectstatic --no-input
python manage.py migrate
