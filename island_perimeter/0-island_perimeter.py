#!/usr/bin/python3
"""
This is the solution to solve the Island Perimeter algorithm
"""


def island_perimeter(grid):
    """Function to solve the Island Perimeter algorithm"""
    a = 0
    number_of_lines = len(grid) - 1
    number_of_columns = len(grid[1]) - 1

    coordinates = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                coordinates.append([i, j])

    for coord in coordinates:
        # droite
        if coord[1] + 1 > number_of_columns or \
           grid[coord[0]][coord[1] + 1] == 0:
            a += 1
        # gauche
        if coord[1] == 0 or grid[coord[0]][coord[1] - 1] == 0:
            a += 1
        # haut
        if coord[0] == 0 or grid[coord[0] - 1][coord[1]] == 0:
            a += 1
        # bas
        if coord[0] + 1 > number_of_lines or grid[coord[0] + 1][coord[1]] == 0:
            a += 1

    return a
