#!/bin/bash
# takes an arg, sends GET req to URL, displays response body
curl -sH "X-School-User-Id: 98" "$1"
