#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total
"""

import math


def makeChange(coins, total):
    """function to solve the algo"""
    if total <= 0:
        return 0

    def moduloNumber(num):
        return num % 2

    if moduloNumber(total) == 1:
        result = list(map(moduloNumber, coins))
        if result.count(0) == len(result):
            return -1

    totalMinusMax = total - max(coins)

    possibleValues = []
    for coin in coins:
        if (totalMinusMax % coin) == 0:
            possibleValues.append(coin)

    if len(possibleValues) == 0:
        return -1

    numberOfCoins = []
    for value in possibleValues:
        numberOfCoins.append(math.floor(totalMinusMax / value))

    return min(numberOfCoins) + 1
