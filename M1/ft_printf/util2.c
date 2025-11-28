/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   util2.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 20:12:57 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/25 20:13:04 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

static unsigned int	ft_le(long unsigned int n)
{
	unsigned int	cont;

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

unsigned int	ft_putnbr_u(unsigned int n)
{
	long unsigned int	i;

	i = n;
	if (i > 9)
	{
		ft_putnbr_u(i / 10);
		ft_putnbr_u(i % 10);
	}
	else
	{
		ft_putchar((i % 10) + '0');
	}
	return (ft_le(n));
}

int	ft_hexmin(unsigned int n)
{
	char	*hex;
	int		count;

	count = 0;
	hex = "0123456789abcdef";
	if (n >= 16)
		count += ft_hexmin(n / 16);
	count += ft_putchar(hex[n % 16]);
	return (count);
}
