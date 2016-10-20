""" Finds the greatest common denominator of two numbers """


def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a % b)

while True:
    num_1 = int(input('Number 1: '))
    num_2 = int(input('Number 2: '))

    print('\nGCD: %d\n' % gcd(num_1, num_2))
