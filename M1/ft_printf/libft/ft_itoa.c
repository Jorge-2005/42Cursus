/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 17:42:13 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/14 17:40:00 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_le(long int n)
{
	int	cont;

	cont = 0;
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n = n / 10;
		cont++;
	}
	return (cont);
}

char	*ft_itoa(int n)
{
	long int	num;
	int			len;
	int			neg;
	char		*arr;

	num = n;
	neg = num < 0;
	if (num < 0)
		num *= -1;
	len = ft_le(num) + neg;
	arr = malloc((len + 1) * sizeof(char));
	if (!arr)
		return (NULL);
	if (neg == 1)
		arr[0] = '-';
	if (num == 0)
		arr[0] = '0';
	arr[len] = '\0';
	while (len > neg)
	{
		arr[--len] = (num % 10) + '0';
		num = num / 10;
	}
	return (arr);
}
/*
int	main(void)
{
	int		i;
	char	*arr;

	arr = ft_itoa(-2147483648);
	i = 0;
	while (arr[i])
	{
		printf("%c", arr[i]);
		i++;
	}
	return (0);
}
*/
