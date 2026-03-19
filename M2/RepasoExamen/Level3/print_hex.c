/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_hex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 16:33:24 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/11 17:26:49 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_atoi(char *str)
{
	int n = 0;

	while (*str != '\0')
	{
		n = n * 10;
		n = n + *str - '0';
		++str;
	}
	return (n);
}

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	print_hex(int	c)
{
	char	arr[] = "0123456789ABCDEF";

	if (c >= 16)
		print_hex(c / 16);
	write(1, &arr[c % 16], 1);
}

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		print_hex(ft_atoi(argv[1]));
		ft_putchar('\n');
	}
	return (0);
}
