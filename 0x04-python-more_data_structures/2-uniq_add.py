#!/usr/bin/bash

def uniq_add(my_list=[]):
    add = 0
    for x in set(my_list):
        add += x
    return add
