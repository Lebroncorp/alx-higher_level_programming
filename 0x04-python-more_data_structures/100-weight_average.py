#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    quantity = 0
    avrag = 0

    for i in my_list:
        avrag += (i[0] * i[1])
        quantity += i[1]
    return (avrag / quantity)
