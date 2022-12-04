#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *listnums, first = 0, last, listlen = 0;

	if (*head == NULL)
		return (1);
	current = *head;
	listnums = malloc(sizeof(int));
	if (listnums == NULL)
		return (0);
	while (current != NULL)
	{
		listnums[listlen] = current->n;
		current = current->next;
		listlen++;
		listnums = realloc(listnums, (1 + listlen) * sizeof(int));
	}
	last = listlen - 1;
	while (listnums[first] == listnums[last])
	{
		first++, last--;
		if (first >= last)
			return (1);
	}
	return (0);
}
