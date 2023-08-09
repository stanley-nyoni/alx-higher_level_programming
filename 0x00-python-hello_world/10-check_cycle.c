#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: singly linked list
*
* Return: 1 if theres cycle, else 0
*/

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *sec = list;

	if (list == NULL)
		return (0);

	while (first && sec && sec->next)
	{
		first = first->next;
		sec = sec->next;
		if (first == sec)
		{
			return (1);
		}
	}
	return (0);
}
