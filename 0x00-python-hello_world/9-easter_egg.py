#!/usr/bin/python3
with open('zen.txt', 'r') as file:
    zen = file.read()
    print("{}".format(zen), end='')
