/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   add_prime_sum.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/09 09:22:56 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/09 11:27:08 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

int	atoi(char *str)
{
	int	i;
	int	num;
	
	i = 0;
	num = 0;
	while (str[i] == ' ')
		i++;
	while (str[i] >= '0' && str[i] <= '9')
	{
		num = (num * 10) + (str[i] - '0');
		i++;
	}
	return (num);
}

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	putnbr(int n)
{
	int	num;

	num = n;
	if (num > 9)
	{
		putnbr(num / 10);
		putnbr(num % 10);
	}
	else
                ft_putchar(num + '0');
}

int	main(int argc, char **argv)
{
	int	i;
	int	num;
	int	j;
	int	cont;
	int	res;

	i = 1;
	res = 0;
	if (argc == 2)
	{
		num = atoi(argv[1]);
		if (num == 1)
			ft_putchar(1 + '0');
		else
		{
			while (i <= num)
			{
				j = 1;
				cont = 0;
				while (j <= i)
				{
					if (i % j == 0)
						cont++;
					j++;
				}
				if (cont == 2)
					res += i;
				i++;
			}
			putnbr(res);
		}
	}
	write(1, "\n", 1);
	return (0);
}
