#!/bin/bash

echo =========== Building base image ===========
docker build --pull --rm -f "../Dockerfile" -t pythondashapp:latest "../."

echo =========== Building dev image ===========
docker build --pull --rm -f "../Dockerfile.dev" -t pythondashapp-dev:latest "../."
