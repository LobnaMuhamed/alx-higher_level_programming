#include "lists.h"
/**
 * insert_node - a function that insert numbers
 * @head: pointer of first node
 * @number: input value
 *
 * Return: return address or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *prev;
	listint_t *new_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!(*head))
	{
		*head = new_node;
		return (*head);
	}
	current = *head;
	prev = NULL;
	while (current && current->n < new_node->n)
	{
		prev  = current;
		current = current->next;
	}
	if (!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = current;
		prev->next = new_node;
	}
	if (current == NULL)
		prev->next = new_node;
	return (new_node);
}
