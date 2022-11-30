#include "lists.h"

/**
 * insert_node - inserts a node into a sorted list
 * @head: pointer to address of head of list
 * @number: integer stored in node
 * Return: address of new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *current;

	current = *head;
	while (current != NULL)
	{
		if (number < current->n)
		{
			new = malloc(sizeof (listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
				if (current == *head)
				{
					new->next = *head;
					*head = new;
					return (new);
				}
			new->next = current;
			temp->next = new;

			return (new);
		}
		temp = current;
		current = current->next;
	}
	add_nodeint_end(head, number);
	return (NULL);
}
