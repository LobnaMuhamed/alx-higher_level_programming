#include "lists.h"

/**
 * check_cycle - a function that check if there a cycle
 * @list: a single linked list
 * Return: return 1 if there is a cycle , 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	if (!list)
		return (-1);
	while (temp)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}
	return (0);

}
