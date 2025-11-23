/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 16:59:55 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/11 20:11:30 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	j;
	size_t	lend;

	i = 0;
	j = ft_strlen(dst);
	lend = ft_strlen(dst);
	if (size <= j)
		return (size + ft_strlen(src));
	if (lend < size)
	{
		while (src[i] && i < (size - lend - 1))
		{
			dst[j] = src[i];
			j++;
			i++;
		}
		dst[j] = '\0';
	}
	return (lend + ft_strlen(src));
}
/*
int	main(void)
{
	char dest[] = "lol";
	char src[] = "nose";
	printf("%d\n", ft_strlcat(dest, src , 4));
	printf("%s\n", dest);
	return (0);
}*/
