#include "lists.h"

size_t dlistint_len(const listint_t *h);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int *dataArr;
	size_t listLength;
	size_t i;
	listint_t *headPtr;

	if (*head == NULL)
	{
		return (1);
	}
	listLength = dlistint_len(*head);
	dataArr = malloc(sizeof(int) * listLength);

	i = 0;
	headPtr = *head;
	while (headPtr != NULL)
	{
		dataArr[i] = headPtr->n;
		headPtr = headPtr->next;
		i++;
	}

	for (i = 0; i < listLength / 2; i++)
	{
		if (dataArr[i] != dataArr[(listLength - i) - 1])
		{
			printf("%lu\n", listLength);
			return (0);
		}
	}
	return (1);
}

/**
 * dlistint_len - returns the number of elements in
 * a double linked list
 *
 * @h: head of the list
 * Return: the number of nodes
 */

size_t dlistint_len(const listint_t *h)
{
	size_t numberOfElements = 0;

	if (h == NULL)
	{
		return (numberOfElements);
	}

	while (h != NULL)
	{
		numberOfElements++;
		h = h->next;
	}
	return (numberOfElements);
}
