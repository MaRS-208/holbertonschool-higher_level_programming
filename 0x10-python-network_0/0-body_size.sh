#!/bin/bash
# Script that takes in a URL and  displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length/ {print $2}'
