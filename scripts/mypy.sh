#!/bin/bash

docker run \
    -v /home/aniculae/WSL-Projects/python-dash-app/config/config.yaml:/app/config/config.yaml \
    -v /home/aniculae/WSL-Projects/python-dash-app/src:/app/src \
    -v /home/aniculae/WSL-Projects/python-dash-app/test:/app/test \
    --env-file /home/aniculae/WSL-Projects/python-dash-app/.env \
    --rm \
    pythondashapp-dev:latest \
    mypy src test
