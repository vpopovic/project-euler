from prime_list import primes

problem_number = 600851475143

for x in primes:
    if problem_number % x == 0:
        print x
