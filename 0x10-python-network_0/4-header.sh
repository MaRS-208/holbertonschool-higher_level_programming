#!/bin/bash
# Takes in URL as argument, sends a GET request and displays body of response
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
