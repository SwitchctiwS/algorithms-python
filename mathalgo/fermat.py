import math


def fermat(n):
    nSqrt = math.ceil(math.sqrt(n))

    a = nSqrt - 1

    integer = False
    while integer is False and a <= n:
        a += 1
        b = math.sqrt(a*a - n)

        if b % 1 == 0:
            integer = True

    arr = []

    if integer is True:
        arr = [a + b, a - b]

    return arr
