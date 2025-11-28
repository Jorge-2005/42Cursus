/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 17:34:44 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/12 17:52:43 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_atoi(const char *nptr)
{
	int	i;
	int	num;
	int	cont;

	i = 0;
	num = 0;
	cont = 1;
	while (nptr[i] == 32 || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '+' || nptr[i] == '-')
	{
		if (nptr[i] == '-')
			cont = -1;
		i++;
	}
	while (nptr[i] >= 48 && nptr[i] <= 57)
	{
		num = (num * 10) + (nptr[i] - '0');
		i++;
	}
	return (num * cont);
}
/*
int	main(void)
{
	printf("%d\n", ft_atoi("    +234hola123"));
	return (0);
}
*/
