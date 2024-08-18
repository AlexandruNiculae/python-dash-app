#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
PROJPATH=$(dirname "$SCRIPTPATH")

docker run \
    -v $PROJPATH/config/config.yaml:/app/config/config.yaml \
    -v $PROJPATH/src:/app/src \
    -v $PROJPATH/data:/app/data \
    --env-file $PROJPATH/.env \
    -p 8050:8050 \
    --rm \
    pythondashapp:latest
