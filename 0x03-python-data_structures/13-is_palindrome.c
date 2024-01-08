#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * test - tests if string characters at end and start are alike.
 * @start: string pointer to be tested
 * @end: string length.
 * @max: number of tests.
 * Return: 1 is all characters match.
 * 0 if otherwise.
 */
int test(int *start, int *end, int max)
{
	if (max == 0)
	{
		return (1);
	}
	else if (*(start) != *(end))
	{
		return (0);
	}
	return (test(start + 1, end - 1, max - 1));
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head pointer of the signly linked list.
 *
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int *list = NULL, count = 1, items, paliflag = 0;
	listint_t *temp;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		list = realloc(list, (count * 4));
		if (list == NULL)
		{
			if (list)
				free(list);
			return (0);
		}
		list[count - 1] = temp->n;
		count++;
		temp = temp->next;
	}
	items = count - 1;
	paliflag = test(&list[0], &list[items - 1], (items / 2));
	free(list);
	return (paliflag);
}
