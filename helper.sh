#!/bin/bash

SCRIPT=$(readlink -f "$0")
PROJPATH=$(dirname "$SCRIPT")
IMAGENAME="pythondashapp"
IMAGETAG="v0"


check_docker() {
    if ! docker info >/dev/null 2>&1; then
        echo "Docker is not running."
        exit 1
    else
        echo "Docker is running."
    fi
}

check_minikube() {
    if ! minikube status >/dev/null 2>&1; then
        echo "Minikube is not running."
        exit 1
    else
        echo "Minikube is running."
    fi
}

build_base_image() {
    echo "Building Docker image inside Minikube..."
    eval $(minikube -p minikube docker-env)
    docker build --pull --rm -f "$PROJPATH/Dockerfile" -t "$IMAGENAME":"$IMAGETAG" "$PROJPATH"
}

build_dev_image() {
    echo "Building Docker image inside Minikube..."
    eval $(minikube -p minikube docker-env)
    docker build --pull --rm -f "$PROJPATH/Dockerfile.dev" -t "$IMAGENAME"-dev:"$IMAGETAG" "$PROJPATH"

}

run_container() {
    echo "Running Docker container from the built image..."
    docker run --rm myimage:latest echo "This is running inside the Docker container."
}

run_mypy() {
    docker run \
    -v $PROJPATH/config/config.yaml:/app/config/config.yaml \
    -v $PROJPATH/src:/app/src \
    -v $PROJPATH/test:/app/test \
    --env-file $PROJPATH/.env \
    --rm \
    "$IMAGENAME"-dev:"$IMAGETAG" \
    mypy src test
}

run_pylint() {
    docker run \
    -v $PROJPATH/config/config.yaml:/app/config/config.yaml \
    -v $PROJPATH/src:/app/src \
    -v $PROJPATH/test:/app/test \
    --env-file $PROJPATH/.env \
    --rm \
    "$IMAGENAME"-dev:"$IMAGETAG" \
    pylint src test
}

run_pytest() {
    docker run \
    -v $PROJPATH/config/config.yaml:/app/config/config.yaml \
    -v $PROJPATH/src:/app/src \
    -v $PROJPATH/test:/app/test \
    --env-file $PROJPATH/.env \
    --rm \
    "$IMAGENAME"-dev:"$IMAGETAG" \
    pytest -s test
}

check_docker
check_minikube

BUILD=0
NODEV=0
TEST=0
LINT=0
MYPY=0

for ARG in "$@"; do
    case $ARG in
        build)
            BUILD=1
            ;;
        --nodev)
            NODEV=1
            ;;
        test)
            TEST=1
            ;;
        lint)
            LINT=1
            ;;
        mypy)
            MYPY=1
            ;;
        *)
            echo "Unknown argument: $ARG"
            echo "Usage: $0 [build] [--nodev] [node=nodename] OR [test/lint/mypy]"
            exit 1
            ;;
    esac
done

if [[ $BUILD -eq 1 ]]; then
    build_base_image
    if [[ $NODEV -eq 0 ]]; then
        build_dev_image
    fi
    exit 0
fi

if [[ $TEST -eq 1 ]]; then
    run_pytest
    exit 0
fi

if [[ $LINT -eq 1 ]]; then
    run_pylint
    exit 0
fi

if [[ $MYPY -eq 1 ]]; then
    run_mypy
    exit 0
fi