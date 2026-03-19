/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 18:16:58 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/05 18:17:01 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

char	*ft_strcpy(char *s1, char *s2)
{
	int	i;
	
	i = 0;
	while (s2[i])
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return (s1);
}

int	main(void)
{
	char hola[] = "sssssssss";
	
	ft_strcpy(hola, "holas");
	printf("%s", hola);
	return (0);
}
