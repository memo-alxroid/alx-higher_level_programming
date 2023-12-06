#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *currentNode;

	if (*head == NULL)
	{
		return (NULL);
	}
	currentNode = *head;
	while (currentNode->next != NULL)
	{
		if (currentNode->n <= number && currentNode->next->n >= number)
		{
			newNode = malloc(sizeof(listint_t));
			if (newNode == NULL)
			{
				return (NULL);
			}
			newNode->n = number;
			newNode->next = currentNode->next;
			currentNode->next = newNode;
			return (newNode);
		}
		currentNode = currentNode->next;
	}
	return (NULL);
}

