/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 20:02:05 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/10 21:01:29 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char		*desti;
	const unsigned char	*srci;
	size_t				i;

	i = 0;
	desti = (unsigned char *)dest;
	srci = (const unsigned char *)src;
	if (!src && !dest)
		return (NULL);
	while (i < n)
	{
		desti[i] = srci[i];
		i++;
	}
	return (desti);
}
/*
int	main(void)
{
	char dest[] = "lol";
	char src[] = "";
	ft_memcpy(dest, src , 5);
	printf("%s", dest);
	return (0);
}
*/
