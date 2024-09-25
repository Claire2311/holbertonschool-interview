#!/usr/bin/python3
"""
This is the solution to solve the Minimum operation algorithm
"""


import math


def minOperations(n) -> int:
    """
    calculates the fewest number of operations needed to result in exactly 
    n H characters in the file
    """
    number_of_operations: int

    if n <= 1:
        number_of_operations = 0
        return number_of_operations

    def is_prime(n) -> bool:
        """check if n is a prime number"""
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    is_n_is_prime = is_prime(n)

    if is_n_is_prime is True:
        number_of_operations = n
        return number_of_operations
    else:
        return n % 2

    return number_of_operations


# print(minOperations(0))
# print(minOperations(1))
# print(minOperations(4))
# print(minOperations(5))
# print(minOperations(6))
# print(minOperations(9))
# print(minOperations(12))
