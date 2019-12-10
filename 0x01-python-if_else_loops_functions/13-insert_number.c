#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * create_node - create a node
 * @node: node
 * @num: num
 */

void create_node(listint_t *node, int num)
{
	node = malloc(sizeof(listint_t));
	node->n = num;
	node->next = NULL;
}

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
		create_node(*head, number);
		return (*head);
	}
	if (number < (*head)->n)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = *head;
		(*head) = new;
		return (*head);
	}
	p = *head;
	while (p->next != NULL)
	{
		if (p->n <= number && p->next->n > number)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			new->next = p->next;
			p->next = new;
			return (new);
		}
		p = p->next;
	}
	if (p->n <= number && p->next == NULL)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = NULL;
		p->next = new;
		return (new);
	}
	return (NULL);
}
