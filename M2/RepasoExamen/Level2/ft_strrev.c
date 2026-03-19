/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 20:41:45 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/07 20:58:09 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

char	*ft_strrev(char *str)
{
	int	i;
	int	end;
	char 	temp;

	i = 0;
	end = 0;
	while (str[end])
		end++;
	end--;
	while (i < end)
	{
		temp = str[i];
		str[i] = str[end];
		str[end] = temp;
		i++;
		end--;
	}
	return (str);
}

int	main(void)
{
	char	str[] = "holas";
	printf("%s", ft_strrev(str));
	return (0);
}
