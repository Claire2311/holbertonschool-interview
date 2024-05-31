/**
 * sandpiles_sum - Computes the sum of two sandpiles and stabilizes the result
 * @grid1: First sandpile (will contain the result)
 * @grid2: Second sandpile
 */

#include <stdio.h>
#include "sandpiles.h"

void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    int i, j;

    // Step 1: Add grid2 to grid1
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid1[i][j] += grid2[i][j];
        }
    }

    // Step 2: Stabilize grid1
    while (1)
    {
        int unstable = 0;
        int temp_grid[3][3] = {0};

        // Check for instability and prepare the toppling
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (grid1[i][j] > 3)
                {
                    unstable = 1;
                    temp_grid[i][j] -= 4;
                    if (i > 0)
                        temp_grid[i - 1][j]++;
                    if (i < 2)
                        temp_grid[i + 1][j]++;
                    if (j > 0)
                        temp_grid[i][j - 1]++;
                    if (j < 2)
                        temp_grid[i][j + 1]++;
                }
            }
        }

        // If no cells are unstable, break out of the loop
        if (!unstable)
            break;

        // Print the unstable grid
        printf("=\n");

        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (j)
                    printf(" ");
                printf("%d", grid1[i][j]);
            }
            printf("\n");
        }

        // Apply the toppling
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                grid1[i][j] += temp_grid[i][j];
            }
        }
    }
}
