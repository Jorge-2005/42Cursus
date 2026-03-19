/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Utils4.c                                            :+:      :+:    :+:  */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	num_bits(int len)
{
	int	max_i;
	int	bits;

	max_i = len - 1;
	bits = 0;
	while (max_i != 0)
	{
		max_i = max_i >> 1;
		bits++;
	}
	return (bits);
}

void	radix_short(t_list **a, t_list **b, int len)
{
	int	max_bits;
	int	i;
	int	j;

	i = 0;
	max_bits = num_bits(len);
	while (i < max_bits)
	{
		j = 0;
		while (j < len)
		{
			if ((((*a)-> index >> i) & 1) == 0)
				pb(a, b);
			else
				ra(a);
			j++;
		}
		while (*b != NULL)
			pa(a, b);
		i++;
	}
}
