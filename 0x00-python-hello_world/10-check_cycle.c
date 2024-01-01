#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	int cycle_flag = 0;

	slow = list->next;
	fast = list->next->next;

	while (fast != NULL)
	{
		if (fast == slow)
		{
			cycle_flag = 1;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (cycle_flag);
}
