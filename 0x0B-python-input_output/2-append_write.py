#!/usr/bin/python3
"""
    Contains the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string to a textfile
    and returns the number of characters appended"""
    append = 0

    with open(filename, "a", encoding="utf-8") as f:
        append = f.write(text)
    return append
