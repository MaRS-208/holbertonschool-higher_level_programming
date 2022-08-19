#!/bin/bash
# Script that takes in URL and displays all HTTP methods the server will accept
curl -sI "$1" | awk '/Allow/ { $1=""; sub(/^[ \t]+/, ""); print }'
