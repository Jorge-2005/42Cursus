/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse.c                                            :+:      :+:    :+: */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	reverse(t_list **list)
{
	t_list	*first;
	t_list	*third;
	t_list	*last;

	if (!list || !*list || !(*list)->next)
		return ;
	first = *list;
	last = ft_lstlast(*list);
	third = last -> prev;
	first -> prev = last;
	last -> next = first;
	last -> prev = NULL;
	third -> next = NULL;
	*list = last;
}

void	rra(t_list **a)
{
	reverse(a);
	write(1, "rra\n", 4);
}

void	rrb(t_list **b)
{
	reverse(b);
	write(1, "rrb\n", 4);
}

void	rrr(t_list **a, t_list **b)
{
	reverse(a);
	reverse(b);
	write(1, "rrr\n", 4);
}
