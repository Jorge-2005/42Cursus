/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:20:10 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/13 17:10:35 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	int		i;
	int		end;	

	i = 0;
	if (!s1 || !set)
		return (NULL);
	end = ft_strlen(s1);
	while (s1[i] && ft_strchr(set, s1[i]))
		i++;
	while (end > i && ft_strchr(set, s1[end - 1]))
		end--;
	return (ft_substr(s1, i, end - i));
}
/*
int	main(void)
{
	printf("%s", ft_strtrim("xxhola quex talexx", "xe"));
	return (0);
}
*/
