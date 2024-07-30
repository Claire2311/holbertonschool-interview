#!/usr/bin/python3
"""
This is the solution to solve the Island Perimeter algorithm
"""


def island_perimeter(grid):
    """Function to solve the Island Perimeter algorithm"""
    a = 0
    number_of_lines = len(grid) - 1
    # print("number_of_lines", number_of_lines)

    coordinates = []

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                coordinates.append([i, j])
    # print("coordinates", coordinates)

    for abs in coordinates:
        # print(grid[abs[0]][abs[1] + 1])  # droite
        # print(grid[abs[0]][abs[1] - 1])  # gauche
        # print(grid[abs[0] - 1][abs[1]])  # haut
        # print(grid[abs[0] + 1][abs[1]])  # bas
        if grid[abs[0]][abs[1] + 1] == 0:
            a += 1
        if grid[abs[0]][abs[1] - 1] == 0:
            a += 1
        if grid[abs[0] - 1][abs[1]] == 0:
            a += 1
        if abs[0] + 1 > number_of_lines or grid[abs[0] + 1][abs[1]] == 0:
            a += 1

    # print(a)
    return a


# grid = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0]
#     ]

# grid = [
#     [0, 2, 3, 4, 5, 6],
#     [0, 1, 8, 9, 10, 11],
#     [12, 1, 13, 14, 15, 16],
#     [17, 0, 0, 0, 18, 19],
#     [20, 21, 22, 23, 24, 25]
#     ]

# grid = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 0, 0]
#     ]

# island_perimeter(grid)
