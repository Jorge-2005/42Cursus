/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	push(t_list **list, t_list **dst)
{
	t_list	*first;

	if (!list || !*list)
		return ;
	first = *list;
	*list = first -> next;
	if (*list)
		(*list)-> prev = NULL;
	first -> next = *dst;
	if (*dst)
		(*dst)-> prev = first;
	first -> prev = NULL;
	*dst = first;
}

void	pa(t_list **a, t_list **b)
{
	push(b, a);
	write(1, "pa\n", 3);
}

void	pb(t_list **a, t_list **b)
{
	push(a, b);
	write(1, "pb\n", 3);
}
