#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
PROJPATH=$(dirname "$SCRIPTPATH")

docker run \
    -v $PROJPATH/config/config.yaml:/app/config/config.yaml \
    -v $PROJPATH/.pylintrc:/app/.pylintrc \
    -v $PROJPATH/src:/app/src \
    -v $PROJPATH/test:/app/test \
    --env-file $PROJPATH/.env \
    --rm \
    pythondashapp-dev:latest \
    pylint src test
