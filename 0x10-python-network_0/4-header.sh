#!/bin/bash

# URL provided as argument
url=$1

# Sending GET request with curl and displaying response body
curl -X GET -H "X-School-User-Id: 98" "$url"
