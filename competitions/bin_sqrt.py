""" Finds the square root of a number with binary search """
import math


def root(num, power=2):
    low = 0
    high = num
    mid = high / 2
    test = mid**power
    dx = 1

    while not math.isclose(test, num, rel_tol=1e-10):
        print(low, mid, high, dx)

        if test < num:
            low = mid + dx
        else:
            high = mid - dx
        mid = (high + low) / 2

        test = mid**power

    return mid


print('Answer:', root(16))
