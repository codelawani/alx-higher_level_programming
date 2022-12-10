#include "lists.h"

/**
 * revlist - reverses a list
 * @node: pointer to middle of list
 * Return: pointer to reversed list
 */

listint_t *revlist(listint_t *node)
{
	listint_t *next, *prev = NULL;

	while (node->next)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	node->next = prev;
	return (node);
}
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to address of head node
 * Return: 1 if it is palindrome or 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *mid, *slow = *head;
	listint_t *fast = *head;
	int i, size = 0;

	if (slow == NULL || slow->next == NULL)
		return (1);
	while (fast != NULL)
	{
		fast = fast->next;
		size++;
	}
	mid = fast = slow->next;
	for (i = 1; i < size / 2; i++)
	{
		slow = slow->next;
		fast = fast->next;
	}
	if (size % 2 != 0)
		fast = fast->next;
	fast = revlist(fast);
	slow = *head;
	while (fast)
	{
		if (slow->n != fast->n)
		{
			revlist(mid);
			return (0);
		}
		slow = slow->next;
		fast = fast->next;
	}
	revlist(mid);
	return (1);
}
