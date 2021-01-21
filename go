#!/bin/bash

source ./venv/bin/activate
export FLASK_APP=myserver.py
python -m flask run -h 0.0.0.0 -p 3975 --reload
