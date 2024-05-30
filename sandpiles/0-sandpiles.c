/**
 * sandpiles_sum - Computes the sum of two sandpiles and stabilizes the result
 * @grid1: First sandpile (will contain the result)
 * @grid2: Second sandpile
 */

#include <stdio.h>
#include "sandpiles.h"

void print_grid(int grid[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (j)
            {
                printf(" ");
            }
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    int grid[3][3];
    int unstable = 1;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            grid[i][j] = grid1[i][j] + grid2[i][j];
        }
    }

    while (unstable)
    {
        unstable = 0;
        int temp[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (grid[i][j] > 3)
                {
                    grid[i][j] -= 4;
                    if (i > 0)
                    {
                        temp[i - 1][j] += 1;
                    }
                    if (i < 2)
                    {
                        temp[i + 1][j] += 1;
                    }
                    if (j > 0)
                    {
                        temp[i][j - 1] += 1;
                    }
                    if (j < 2)
                    {
                        temp[i][j + 1] += 1;
                    }
                    unstable = 1;
                }
            }
        }

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                grid[i][j] += temp[i][j];
            }
        }

        print_grid(grid);
        printf("\n");
    }
}