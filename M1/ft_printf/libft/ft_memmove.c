/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 21:01:57 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/11 16:07:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t				i;
	unsigned char		*desti;
	const unsigned char	*srci;

	desti = (unsigned char *)dest;
	srci = (const unsigned char *)src;
	i = 0;
	if (!dest && !src)
		return (NULL);
	if (dest > src)
	{
		while (n-- > 0)
			desti[n] = srci[n];
	}
	else
	{
		while (i < n)
		{
			desti[i] = srci[i];
			i++;
		}
	}
	return (dest);
}
/*
int	main(void)
{
	char dest[] = "l";
	char src[] = "a";
	ft_memmove(dest, src, 4);
	printf("%s", dest);
	return (0);
}
*/
