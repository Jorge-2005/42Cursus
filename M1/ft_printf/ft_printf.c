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
	else if (str == 'p')
		return (ft_putpoint(va_arg(args, void *)));
	else if (str == 'd' || str == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (str == 'u')
		return (ft_putnbr_u(va_arg(args, unsigned int)));
	else if (str == 'x')
		return (ft_hexmin(va_arg(args, unsigned int)));
	else if (str == 'X')
		return (ft_hex(va_arg(args, unsigned int)));
	else if (str == '%')
		return (ft_putchar('%'));
	return (0);
}

int	ft_printf(const char *type, ...)
{
	int		i;
	int		len;
	va_list	args;

	i = -1;
	len = 0;
	va_start(args, type);
	while (type[++i])
	{
		if (type[i] == '%' && type[i + 1])
		{
			len += ft_findtype(type[i + 1], args);
			i++;
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
	//int	x = 0;
	//int	*p = &x;
 
	ft_printf("%p\n", 0);
	printf("%p", (void *)0);
	return (0);
}
*/
/*
int main(void)
{
	int x = 0;
	int *p = &x;
	ft_printf("%c\n", 'a');
	printf("%c\n", 'a');
	ft_printf("%s\n", "pepe");
	printf("%s\n", "pepe");
	ft_printf("%d\n", 13);
	printf("%d\n", 13);
	ft_printf("%p\n", p);
	printf("%p\n", p);
	ft_printf("%i\n", -14);
	printf("%i\n", -14);
	ft_printf("%u\n", 15);
	printf("%u\n", 15);
	ft_printf("%x\n", 'd');
	printf("%x\n", 'd');
	ft_printf("%X\n", 'D');
	printf("%X\n", 'D');
	ft_printf("%%\n");
	printf("%%\n");
}*/
