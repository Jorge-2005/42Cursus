/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strspn.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 22:34:33 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/07 23:00:15 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

size_t	ft_strspn(const char *s, const char *accept)
{
	int	i;
	int	j;
	int	cont;
	int	boolean;

	i = 0;
	cont = 0;
	while (s[i])
	{
		j= 0;
		boolean = 0;
		while (accept[j])
		{
			if (s[i] == accept[j])
			{
				cont++;
				boolean = 1;
			}
			j++;
		}
		if (boolean == 0)
			return (cont);
		i++;
	}
	return (cont);
}

int	main(void)
{
	printf("%zu",ft_strspn("hola", "hoslas"));
	return (0);
}
