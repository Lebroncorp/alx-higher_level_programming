#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    call = 0

    for i in range(x):
        if (isinstance(my_list[i], int)):
            try:
                print("{:d}".format(my_list[i]), end="")
                call += 1

            except (IndexError):
                raise IndexError("list out of range")
    print()
    return (call)
