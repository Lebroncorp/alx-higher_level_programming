#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if b == a:
            continue
        print("{:d}{:d}".format(a, b), end=', ')
print()
