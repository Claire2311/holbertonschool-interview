#ifndef SORT_H
#define SORT_H

#include <stddef.h> 

// Function prototypes
void countingSort(int *array, size_t size, int exp);
void radix_sort(int *array, size_t size);
void print_array(const int *array, size_t size); 

#endif
