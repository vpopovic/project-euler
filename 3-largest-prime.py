"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(a):
    return all(a % i for i in xrange(2, a))


def is_divisible(x, y):
    return x % y == 0
