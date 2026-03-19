/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   util.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 17:30:33 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/25 17:30:41 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_putchar(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_putstr(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (write (1, "(null)", 6));
	while (s[i])
	{
		ft_putchar(s[i]);
		i++;
	}
	return (i);
}

static int	ft_le(long int n)
{
	int	cont;

	cont = 0;
	if (n < 0)
	{
		cont++;
		n *= -1;
	}
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n = n / 10;
		cont++;
	}
	return (cont);
}

int	ft_putnbr(int n)
{
	long int	i;

	i = n;
	if (i < 0)
	{
		ft_putchar('-');
		i *= -1;
	}
	if (i > 9)
	{
		ft_putnbr(i / 10);
		ft_putnbr(i % 10);
	}
	else
		ft_putchar((i % 10) + '0');
	return (ft_le(n));
}

int	ft_hex(unsigned int n)
{
	char	*hex;
	int		count;

	count = 0;
	hex = "0123456789ABCDEF";
	if (n >= 16)
		count += ft_hex(n / 16);
	count += ft_putchar(hex[n % 16]);
	return (count);
}
