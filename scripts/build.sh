#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
PROJPATH=$(dirname "$SCRIPTPATH")

echo =========== Building base image ===========
docker build --pull --rm -f "$PROJPATH/Dockerfile" -t pythondashapp:latest "$PROJPATH"

echo =========== Building dev image ===========
docker build --pull --rm -f "$PROJPATH/Dockerfile.dev" -t pythondashapp-dev:latest "$PROJPATH"
