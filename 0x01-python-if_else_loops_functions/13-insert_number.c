#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * insert_node - insert a node in a list
 * @head: head of list
 * @number: number to add
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new = NULL, *p = NULL;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	p = *head;
	while (p != NULL)
	{
		if (p->n <= number && p->next->n >= number)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			new->next = p->next;
			p->next = new;
			break;
		}
		p = p->next;
	}

	if (p == NULL)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = NULL;
		p->next = new;
	}
	return (new);
}