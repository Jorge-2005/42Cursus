/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 12:11:57 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/13 15:13:59 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		i;
	int		j;
	char	*arr;

	i = 0;
	j = 0;
	arr = malloc(((ft_strlen(s1) + ft_strlen(s2)) + 1) * sizeof(char));
	if (!arr)
		return (NULL);
	while (s1[i])
	{
		arr[i] = s1[i];
		i++;
	}
	while (s2[j])
	{
		arr[i] = s2[j];
		j++;
		i++;
	}
	arr[i] = '\0';
	return (arr);
}
/*
int	main(void)
{
	char	*arr;
	int	i;

	i = 0;
	arr = ft_strjoin("locura", "maxima");

	while (arr[i])
	{
		printf("%c", arr[i]);
		i++;
	}
	return (0);
}
*/
