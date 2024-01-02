#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * place_node - places the node at the right place in the list.
 */

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head pointer of the linked list.
 * @number: the number to be insterted to the list.
 *
 * Return: the address of the new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1, *tmp2, *new;

	/** check if head or *head is NULL **/
	if (head == NULL)
		return (NULL);
	/** create a new node with number **/
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	/** assigning the values to the node **/
	new->n = number;
	new->next = NULL;
	/** if list is empty **/
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	/** assigning 2 tmp pointers **/
	tmp1 = *head;
	tmp2 = (*head)->next;
	/** if list has one node **/
	if (tmp2 == NULL)
	{
		if ((*head)->n > number)
		{
			*head = new;
			new->next = tmp1;
			return (new);
		}
		else
		{
			(*head)->next = new;
			return (new);
		}
	}
	/** inserting in middle of list **/
	while (tmp2 != NULL)
	{
		if (tmp1->n <= number && tmp2->n >= number)
		{
			tmp1->next = new;
			new->next = tmp2;
			return (new);
		}
		else if (number <= tmp1->n && number <= tmp2->n)
		{
			*head = new;
			new->next = tmp1;
			return (new);
		}
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	/** inserting at end of list **/
	tmp1->next = new;
	return (new);
}
