/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   is_power_of_2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 23:27:43 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/07 23:39:21 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	is_power_of_2(unsigned int n)
{
	unsigned int	num;

	num = 1;
	while (num < n)
		num = num * 2;
	if (num == n)
		return (1);
	return (0);
}

int	main(void)
{
	printf("%d", is_power_of_2(1));
	return (0);
}
