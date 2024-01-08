#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head pointer of the signly linked list.
 *
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int *list = NULL, count = 1, items, i = 0, paliflag = 1;
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
	for (i = 0; i < (items / 2); i++)
	{
		if (list[items - 1 - i] == list[i])
			continue;
		else
			paliflag = 0;
	}
	free(list);
	return (paliflag);
}
