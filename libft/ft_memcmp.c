/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 22:09:32 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/12 17:04:57 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				i;
	const unsigned char	*s;
	const unsigned char	*q;

	i = 0;
	s = (unsigned char *)s1;
	q = (unsigned char *)s2;
	while (i < n && s[i] == q[i])
		i++;
	if (i == n)
		return (0);
	return (s[i] - q[i]);
}
/*
int	main(void)
{
	printf("%d", ft_memcmp("hola", "hola", 5));
	return (0);
}
*/
