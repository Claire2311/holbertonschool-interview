#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL, *next = NULL;

    while (head) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }

    return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head) {
    if (!head || !(*head)) {
        return 1; // An empty list is considered a palindrome
    }

    listint_t *slow = *head, *fast = *head, *second_half, *reversed_half;
    listint_t *first_half = *head;

    // Find the middle of the list
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // If odd number of nodes, skip the middle node
    if (fast) {
        slow = slow->next;
    }

    // Reverse the second half of the list
    reversed_half = reverse_list(slow);

    // Compare the first half and the reversed second half
    second_half = reversed_half;
    while (second_half) {
        if (first_half->n != second_half->n) {
            reverse_list(reversed_half); // Restore the list before returning
            return 0; // Not a palindrome
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the list by reversing the second half back
    reverse_list(reversed_half);

    return 1; // It's a palindrome
}
