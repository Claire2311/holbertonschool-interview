#ifndef SORT_H
#define SORT_H

#include <stddef.h> // For size_t

// Function prototypes
void countingSort(int *array, size_t size, int exp);
void radix_sort(int *array, size_t size);
void printArray(const int *array, size_t size); // Assuming printArray is defined elsewhere

#endif /* SORT_H */