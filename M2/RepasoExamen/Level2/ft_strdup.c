/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 20:07:40 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/07 20:14:30 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char	*str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	int	i;
	char	*arr;

	i = 0;
	arr = malloc((ft_strlen(src) + 1) * sizeof(char));
	if (!arr)
		return (NULL);
	while (src[i])
	{
		arr[i] = src[i];
		i++;
	}
	arr[i] = '\0';
	return (arr);
}

int	main(void)
{
	printf("%s", ft_strdup("hola uqe tal"));
	return (0);
}
