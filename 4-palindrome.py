"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99. Find the largest palindrome made from the product
of two 3-digit numbers.
"""


def check_palindrome(number):
    return True if str(number) == str(number)[::-1] else False


biggest_palindrome = 0
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        if check_palindrome(x * y) and (x * y) > biggest_palindrome:
            biggest_palindrome = (x * y)

print(biggest_palindrome)
