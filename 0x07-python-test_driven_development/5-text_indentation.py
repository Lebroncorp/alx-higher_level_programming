#!/usr/bin/python3
"""
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for c in text:
        if flag == 0:
            if c == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
