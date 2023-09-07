#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    a = 10
    b = 5

    adda = add(a, b)
    suba = sub(a, b)
    mula = mul(a, b)
    diva = div(a, b)

print(f"{a} + {b} = {adda}")
print(f"{a} + {b} = {suba}")
print(f"{a} + {b} = {mula}")
print(f"{a} + {b} = {diva}")
