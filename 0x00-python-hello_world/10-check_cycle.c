#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to head of linked list
 * @Return: 1 if cycle exits, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
