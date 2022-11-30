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
	while (current->n < number && current != NULL)
	{
		temp = current;
		current = current->next;
	}
	if (current == NULL)
		return (NULL);
	new = malloc(sizeof (listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = current;
	temp->next = new;
	
	return (new);
}
