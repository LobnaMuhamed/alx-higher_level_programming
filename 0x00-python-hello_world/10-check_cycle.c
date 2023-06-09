#include "lists.h"

/**
 * check_cycle - a function that check if there a cycle
 * @list: a single linked list
 * Return: return 1 if there is a cycle , 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list, *current;

	if (!list || !temp->next)
		return (0);
	current = list->next;

	while (temp && current && current->next)
	{
		if (temp == current)
			return (1);

		temp = temp->next;
		current = current->next->next;
	}
	return (0);

}
