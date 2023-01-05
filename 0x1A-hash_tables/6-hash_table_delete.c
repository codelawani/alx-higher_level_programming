#include "hash_tables.h"

/**
 * hash_table_get - retrieves a value associated with a key.
 * @ht: hash table
 * @key: key to access value
 *
 * Return: value associated with the element,
 * or NULL if key couldn’t be found
 */

void hash_table_delete(hash_table_t *ht)
{
	unsigned long int i;
	hash_node_t *tmp, *node = NULL;

	for (i = 0; i < ht->size; i++)
	{
		node = ht->array[i];
		while (node != NULL)
		{
			free(node->key);
			free(node->value);
			tmp = node;
			node = node->next;
			free(tmp);
		}
	}
	free(ht->array);
	free(ht);
}
