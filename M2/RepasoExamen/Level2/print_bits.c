/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 21:02:19 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/08 21:09:55 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <unistd.h>

void	print_bits(unsigned char octect)
{
	int	i;
	int	bit;

	i = 8;
	while (i >= 0)
	{
		bit = (octect >> i) & 1;
		bit = bit + '0';
		write(1, &bit, 1);
		i--;
	}
}

int	main(void)
{
	print_bits(2);
	return (0);
}
