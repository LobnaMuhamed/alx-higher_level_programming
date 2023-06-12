#include "lists.h"
/**
 * is_palindrome - a function that checks if a list is palindrome
 * @head: entry linked list
 *
 * Return: return 0 if it's not , 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int stack[1024], i = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	while (temp)
	{
		i++;
		stack[i] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	while (temp)
	{
		if (temp->n != stack[i])
			return (0);
		temp = temp->next;
		i--;
	}
	return (1);
}
