#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 *
 * @head: A pointer pointing to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *current, *prev = NULL;

	while (node)
	{
		current = node->next;
		node->next = prev;
		prev = node;
		node = current;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to the head of the list.
 *
 * Return: If the linked list is not a palindrome - 0 else -1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *main;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	rev = reverse_list(&tmp);
	main = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_list(&main);

	return (1);
}
