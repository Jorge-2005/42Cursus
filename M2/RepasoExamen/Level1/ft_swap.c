/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 18:38:16 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/05 18:47:11 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	ft_swap(int *a, int *b)
{
	int	c;
	c = *b;
	*b = *a;
	*a = c;
}

int	main(void)
{
	int	a = 1;
	int	b = 4;

	ft_swap(&a, &b);
	printf("%i", a);
	printf("%i", b);
	return (0);
}
