#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    a = 10
    b = 5

    adda = add(a, b)
    suba = sub(a, b)
    mula = mul(a, b)
    diva = div(a, b)

print("{} + {} = {}".format(a, b, adda))
print("{} + {} = {}".format(a, b, suba))
print("{} + {} = {}".format(a, b, mula))
print("{} + {} = {}".format(a, b, diva))
