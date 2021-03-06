#include "lists.h"

/**
  * check_cycle - find if a list has a loop
  * @list : head of the list
  * Return: an int
  */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fast != NULL && slow != NULL && slow->next->next && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
		return (1);
	}
return (0);
}
