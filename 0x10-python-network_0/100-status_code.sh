#!/bin/bash
# Sends request to URL as argument, and displays only status code of response
curl -s -o /dev/null -w "%{http_code}" $1

