/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fizzbuzz.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 20:47:23 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/04 20:47:45 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	put_char(char c)
{
	write(1, &c, 1);
}

void	putnbr(int nb)
{
	if (nb <= 9 && nb >= 0)
		put_char(nb + '0');
	else
	{
		putnbr(nb / 10);
		putnbr(nb % 10);
	}
}

int	main(void)
{
	int	i;
	
	i = 1;
	while (i <= 100)
	{
		if (i % 3 == 0 && i % 5 == 0)
			write(1, "fizzbuzz", 8);
		else if (i % 3 == 0)
			write(1, "fizz", 4);
		else if (i % 5 == 0)
			write(1, "buzz", 4);
		else
			putnbr(i);
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
