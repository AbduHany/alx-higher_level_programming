#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * totail - reaches the tail of a linked list through recursion.
 * @head: pointer to head pointer of linked list.
 * @tail: tail pointer of linked list.
 * Return:
 */
void totail(listint_t *tail, listint_t **head, int *paliflag)
{
	if (tail == NULL)
		return;
	totail(tail->next, head, paliflag);
	if (tail->n != (*head)->n)
	{
		*paliflag = 0;
	}
	(*head) = (*head)->next;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head pointer of the signly linked list.
 *
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int paliflag = 1;
	listint_t **temp, *tail;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	temp = head;
	tail = *head;
	totail(tail, temp, &paliflag);
	return (paliflag);
}
