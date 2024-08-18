#!/bin/bash

docker run \
    -v /home/aniculae/WSL-Projects/python-dash-app/config/config.yaml:/app/config/config.yaml \
    -v /home/aniculae/WSL-Projects/python-dash-app/src:/app/src \
    --env-file /home/aniculae/WSL-Projects/python-dash-app/.env \
    -p 8050:8050 \
    --rm \
    pythondashapp:latest
