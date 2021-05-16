from math import *
from decimal import *

def calculate(x):
    return x ** 19 - 1.9 ** x

def halving(start, stop, decimals):
    a = start
    b = stop

    while True:
        mid = (a+b)/2

        if calculate(a) * calculate(mid) < 0:
            b = mid
        else:
            a = mid

        if round(a, ndigits=decimals) == round(b, ndigits=decimals):
            break

    return round(a, ndigits=decimals)


def iterate(a, b, depth, ndigits, seeklimit=False, closetolimit=0):

    result = (b + (a/b)) / 2
    # print(result, f"x={10-i}")

    if seeklimit and round(b, ndigits) == round(result, ndigits):
        print(round(result, ndigits))
        closetolimit += 1

        if depth > 0 and closetolimit < 10:
            iterate(a, result, depth - 1, ndigits, seeklimit, closetolimit)

    else:
        print(result)
        if depth > 0:
            iterate(a, result, depth - 1, ndigits, seeklimit, closetolimit=0)


def an2xan1(x, previous, depth, ndigits, seeklimit=False, closetolimit=0):

    result = previous * x
    # print(result, f"x={10-i}")

    if seeklimit and round(x, ndigits) == round(result, ndigits):
        print(round(result, ndigits))
        closetolimit += 1

        if depth > 0 and closetolimit < 10:
            iterate(result, x, depth - 1, ndigits, seeklimit, closetolimit)

    else:
        print(result)
        if depth > 0:
            an2xan1(result, x, depth - 1, ndigits, seeklimit, closetolimit=0)


def newton(x, depth, ndigits, seeklimit=False, closetolimit=0):
    value = x**3 - 3
    derivative = 3 * x**2

    result = x - value / derivative




    if seeklimit and round(result, ndigits) == round(x, ndigits):
        print(round(result, ndigits))
        closetolimit += 1

        if depth > 0 and closetolimit < 10:
            newton(result, depth - 1, ndigits, seeklimit, closetolimit)

    else:
        print(result)
        if depth > 0:
            newton(result, depth - 1, ndigits, seeklimit)


def kiintopiste(x, depth, ndigits, seeklimit=False, closetolimit=0):

    result = log(sin(x)) + 2

    if seeklimit and round(result, ndigits) == round(x, ndigits):
        print(round(result, ndigits))
        closetolimit += 1

        if depth > 0 and closetolimit < 10:
            kiintopiste(result, depth - 1, ndigits, seeklimit, closetolimit)

    else:
        print(result)
        if depth > 0:
            kiintopiste(result, depth - 1, ndigits, seeklimit)


# iterate(3, 4, 100, ndigits=2, seeklimit=True)
# an2xan1(2, 2/3, depth=50, ndigits=6)
# newton(x=1, depth=50, ndigits=3, seeklimit=True)
kiintopiste(1.9, depth=70, ndigits=4, seeklimit=True)
