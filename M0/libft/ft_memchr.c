/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 21:33:18 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/11 22:09:02 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*si;

	i = 0;
	si = (unsigned char *)s;
	while (i < n)
	{
		if (si[i] == (unsigned char)c)
			return (&si[i]);
		i++;
	}
	return (NULL);
}
/*
int	main(void)
{
	void *res= ft_memchr("lola", 97, 3);
	printf("%s\n",(unsigned char *)res);
	return (0);
}
*/
