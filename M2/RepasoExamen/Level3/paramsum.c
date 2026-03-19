/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   paramsum.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/09 13:30:37 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/09 13:37:48 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void 	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	putnbr(int num)
{
	int	n;

	n = num;
	if (n >= 10)
	{
		putnbr(n / 10);
		putnbr(n % 10);
	}
	else
		ft_putchar(n + '0');
}

int	main(int argc, char **argv)
{
	(void)argv;

	putnbr(argc - 1);
	ft_putchar('\n');
	return (0);
}
