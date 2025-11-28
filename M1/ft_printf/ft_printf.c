/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 17:23:18 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/24 18:56:45 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_findtype(const char str, va_list args)
{
	if (str == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (str == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (str == 'd' || str == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (str == 'u')
		return (ft_putnbr_u(va_arg(args, unsigned int)));
	else if (str == 'x')
		return (ft_hexmin(va_arg(args, int)));
	else if (str == 'X')
		return (ft_hex(va_arg(args, int)));
	else if (str == '%')
		return (ft_putchar('%'));
	return (0);
}

int	ft_printf(const char *type, ...)
{
	int		i;
	int		boolean;
	int		len;
	va_list	args;

	i = -1;
	boolean = 0;
	len = 0;
	va_start(args, type);
	while (type[++i])
	{
		if (type[i] == '%' && type[i + 1])
		{
			len += ft_findtype(type[i + 1], args);
			i++;
			boolean = 1;
		}
		else
			len += ft_putchar(type[i]);
	}
	va_end(args);
	return (len);
}
/*
int	main(void)
{
	ft_printf("%X", -255);
	//printf(" que pasa%w");
	return (0);
}
*/
