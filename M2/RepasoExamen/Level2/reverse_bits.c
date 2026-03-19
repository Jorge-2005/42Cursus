/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_bits.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 21:13:00 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/08 21:13:01 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <unistd.h>

unsigned char	reverse_bits(unsigned char octect)
{
	int	i;
	int	bit;
	unsigned char	res;

	i = 0;
	res = 0;
	while (i < 8)
	{
		bit = (octect >> i) & 1;
		res = res * 2 + bit;
		i++;
	}
	return (res);
}

int	main(void)
{
	unsigned char hola = reverse_bits(2);
	printf("%d\n", hola);
	return (0);
}
