#!/bin/bash

echo "Starting App"

poetry run python manage.py run -p 8000 -h 0.0.0.0
