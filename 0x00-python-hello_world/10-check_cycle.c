#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - checks if list cyclical
* @list: pointer
* Return: 1 (success)
*/

int check_cycle(listint_t *list)
listint_ *alwo = list;
*fast  = list;
while (fast && fast->next)
{
alwo = alwo->next;
fast = fast->next->next;
if (alwo == fast)
return (1);
}
return (0);
}
