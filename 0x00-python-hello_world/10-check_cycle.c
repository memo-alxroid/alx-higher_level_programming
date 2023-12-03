#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer of the start of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *previousNode;
	listint_t *nextNode;

	previousNode = list;
	nextNode = list;

	while (previousNode && nextNode && nextNode->next->next)
	{
		previousNode = previousNode->next;
		nextNode = nextNode->next->next;

		if (previousNode == nextNode)
		{
			return (1);
		}
	}
	return (0);
}
