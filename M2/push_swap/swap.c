/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	swap(t_list **list)
{
	t_list	*first;
	t_list	*second;
	t_list	*third;

	if (!list || !*list || !(*list)->next)
		return ;
	first = *list;
	second = first->next;
	third = second->next;
	*list = second;
	second -> prev = NULL;
	second -> next = first;
	first -> prev = second;
	first ->next = third;
	if (third)
		third -> prev = first;
}

void	sa(t_list **a)
{
	swap(a);
	write(1, "sa\n", 3);
}

void	sb(t_list **b)
{
	swap(b);
	write(1, "sb\n", 3);
}

void	ss(t_list **a, t_list **b)
{
	swap(a);
	swap(b);
	write(1, "ss\n", 3);
}
