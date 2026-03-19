/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Utils.c                                             :+:      :+:    :+:  */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

t_list	*ft_lstnew(int value)
{
	t_list	*arr;

	arr = malloc(sizeof(t_list));
	if (!arr)
		return (NULL);
	arr -> value = value;
	arr -> next = NULL;
	arr -> prev = NULL;
	return (arr);
}

t_list	*ft_lstlast(t_list *list)
{
	if (!list)
		return (NULL);
	while (list -> next)
		list = list -> next;
	return (list);
}

void	ft_lstadd_back(t_list **list, t_list *new)
{
	t_list	*last;

	if (!list || !new)
		return ;
	if (*list == NULL)
	{
		*list = new;
		(*list)-> prev = NULL;
	}
	else
	{
		last = ft_lstlast(*list);
		last -> next = new;
		new -> prev = last;
	}
}

void	ft_error(void)
{
	write(1, "Error\n", 6);
	exit (1);
}
