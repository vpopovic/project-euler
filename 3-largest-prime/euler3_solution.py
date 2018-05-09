"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from prime_list import primes

problem_number = 600851475143

for x in primes:
    if problem_number % x == 0:
        print(x)
