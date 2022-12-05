#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointer to address of the head of the list
 * Return: 1 if palindrome or 0 if not
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j, count = 0;
	listint_t *front, *rear, *current;

	if (*head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	while (i != count / 2)
	{
		front = rear = *head;
		for (j = 0 ; j < i ; j++)
			front = front->next;
		for (j = 0 ; j < count - (i + 1) ; j++)
			rear = rear->next;
		if (front->n != rear->n)
			return (0);
		else
			i++;
	}
	return (1);
}
