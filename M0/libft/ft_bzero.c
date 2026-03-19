/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 19:18:53 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/10 19:26:07 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	int				i;
	unsigned char	*temp;

	i = 0;
	temp = (unsigned char *)s;
	while (n > 0)
	{
		temp[i] = 0;
		i++;
		n--;
	}
}
/*
int	main(void)
{
	char str[] = "locura";
	ft_bzero(str, 4);
	printf("%s", str);
	return (0);
}
*/
