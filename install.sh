#!/bin/bash

echo "Creating python virtual environement"
python3 -m venv ./venv
sleep 1s
source $(pwd)"/venv/bin/activate"
sleep 2s
echo "Installing project's dependencies"
poetry env use $(pwd)"/venv/bin/python"
sleep 1s
poetry install
echo "installing pre commit hooks"
pre-commit install
