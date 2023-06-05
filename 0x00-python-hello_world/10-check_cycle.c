#include "lists.h"

/**
 * check_cycle - a function that check if there a cycle
 * @list: a single linked list
 * Return: return 1 if there is a cycle , 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *temp, *current;

	temp = list->next;
	current = temp->next;

	if (!list || !temp)
		return (0);
	while (temp && current && current->next)
	{
		if (temp == list)
			return (1);

		temp = temp->next;
		current = current->next->next;
	}
	return (0);

}
