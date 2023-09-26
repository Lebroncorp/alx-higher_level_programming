#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    resolve = None
    try:
        resolve = fct(*args)

    except Exception as errors:
        errors = errors.args[0]
        sys.stderr.write("Exception: " + errors + "\n")

    return (resolve)
