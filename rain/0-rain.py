#!/usr/bin/python3

def rain(walls: list[int]) -> int:
    """calculate how many square units of water will be retained
    after it rains"""
    if not walls:
        return 0

    walls_index = []

    for index, wall in enumerate(walls):
        if wall != 0:
            walls_index.append(index)

    square_of_rain = 0

    for index, square in enumerate(walls_index):
        if index == 0:
            pass
        if index == len(walls_index)-1:
            return square_of_rain
        square_of_rain += (
            (walls_index[index+1] - walls_index[index] - 1) *
            min(walls[walls_index[index]], walls[walls_index[index+1]])
        )

    return square_of_rain
