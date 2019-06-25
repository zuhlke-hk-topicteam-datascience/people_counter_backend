#!/bin/bash

while test $# -gt 0; do
    case "$1" in
        -D|--debug)
            export FLASK_DEBUG=1
            shift
            ;;
        *)
            break
            ;;
    esac
done

export FLASK_APP="flaskr"

flask run