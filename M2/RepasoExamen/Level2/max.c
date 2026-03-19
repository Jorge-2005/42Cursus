/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 20:21:36 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/08 20:29:41 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	max(int *tab, unsigned int len)
{
	unsigned int	i;
	int	max;

	i = 0;
	max = tab[0];
	while (i < len)
	{
		if (max < tab[i])
			max = tab[i];
		i++;
	}
	return (max);
}

int	main(void)
{
	int	i[] ={9,11,10,12};

	printf("%d", max(i, 4));
	return (0);
}
