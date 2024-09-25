#!/usr/bin/python3
"""
This is the solution to solve the Minimum operation algorithm
"""


import math
from typing import List


def minOperations(n) -> int:
    """
    calculates the fewest number of operations needed to result in exactly 
    n H characters in the file
    """
    number_of_operations: int = 0
    list_of_operations: List[int] = []
    list_of_multiples: List[int] = []

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

    def smallest_multiple(num) -> int:
        """return the smallest multiple of a number"""
        for i in range(2, num):
            if num % i == 0:
                list_of_multiples.append(i)
                return i

    if is_prime(n) is True:
        number_of_operations = n
        return number_of_operations

    while is_prime(n) is False:
        n = int(n / smallest_multiple(n))
        list_of_operations.append(n)

    list_of_multiples.append(list_of_operations[len(list_of_operations)-1])

    for multiple in list_of_multiples:
        number_of_operations += multiple

    return number_of_operations
