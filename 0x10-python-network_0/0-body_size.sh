#!/bin/bash
# It ends a request to the URL that displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
