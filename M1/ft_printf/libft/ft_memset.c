/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:49:59 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/10 19:17:43 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*temp;

	i = 0;
	temp = (unsigned char *)s;
	while (n > 0)
	{
		temp[i] = (unsigned char)c;
		i++;
		n--;
	}
	return (temp);
}
/*
int	main(void)
{
	char str[]= "locura";
	ft_memset(str, 97, 4);
	printf("%s\n", str);
	return (0);
}
*/
