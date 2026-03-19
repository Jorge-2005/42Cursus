/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   short.c                                             :+:      :+:    :+:  */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	size3(t_list **list_a)
{
	int	a;
	int	b;
	int	c;

	a = (*list_a)-> value;
	b = (*list_a)-> next-> value;
	c = (*list_a)-> next-> next-> value;
	if (a > b && b < c && a < c)
		sa(list_a);
	else if (a > b && b > c)
	{
		sa(list_a);
		rra(list_a);
	}
	else if (a > b && b < c && a > c)
		ra(list_a);
	else if (a < b && b > c && a < c)
	{
		sa(list_a);
		ra(list_a);
	}
	else if (a < b && b > c && a > c)
		rra(list_a);
}

int	size4(t_list **list_a)
{
	int		min;
	int		pos;
	int		real_pos;
	t_list	*first;

	real_pos = 0;
	pos = 0;
	first = (*list_a);
	min = (*list_a)-> value;
	while (first)
	{
		if (min > first-> value)
		{
			min = first-> value;
			real_pos = pos;
		}
		first = first -> next;
		pos++;
	}
	return (real_pos);
}

void	short_size4(t_list **list_a, t_list **list_b, int real_pos)
{
	if (real_pos == 1)
		ra(list_a);
	else if (real_pos == 2)
	{
		ra(list_a);
		sa(list_a);
	}
	else if (real_pos == 3)
		rra(list_a);
	pb(list_a, list_b);
	size3(list_a);
	pa(list_a, list_b);
}

void	size5(t_list **list_a)
{
	int	pos;

	pos = size4(list_a);
	if (pos == 1)
		ra(list_a);
	else if (pos == 2)
	{
		ra(list_a);
		sa(list_a);
	}
	else if (pos == 3)
	{
		rra(list_a);
		rra(list_a);
	}
	else if (pos == 4)
		rra(list_a);
}
