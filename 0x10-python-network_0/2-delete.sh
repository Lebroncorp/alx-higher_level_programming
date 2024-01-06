#!/bin/bash
# sends DELETE request to 1st URL arg and display response body
curl -s "$1" -X DELETE
