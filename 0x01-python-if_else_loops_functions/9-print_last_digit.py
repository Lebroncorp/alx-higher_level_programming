#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    l_d = abs(number) % 10
    print(f"{l_d}", end='')

    return l_d
