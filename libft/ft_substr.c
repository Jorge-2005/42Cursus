/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 20:06:40 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/13 12:10:08 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	i;
	char	*arr;

	i = 0;
	if (!s)
		return (NULL);
	if (ft_strlen(s) <= start)
	{
		arr = ft_strdup("");
		return (arr);
	}
	if (len > ft_strlen(s) - start)
		len = ft_strlen(s) - start;
	arr = malloc((len + 1) * sizeof(char));
	if (!arr)
		return (NULL);
	while (i < len && s[start + i])
	{
		arr[i] = s[start + i];
		i++;
	}
	arr[i] = '\0';
	return (arr);
}
/*
int	main(void)
{
	int	len = 7;
	char	*arr = ft_substr("hola que tal", 8 , len);
	printf("%s\n", arr);
	return (0);
}
*/
