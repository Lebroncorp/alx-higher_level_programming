#!/bin/bash
# sends GET request to URL to display response body
curl -sfL "$1" -X GET
