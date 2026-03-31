#!/bin/bash

. ~/projects/solar_project/solar_venv/bin/activate

python ~/projects/solar_project/solarterra/manage.py runserver &

sleep 3

chromium-gost