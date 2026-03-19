/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprime.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 19:23:28 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/12 20:37:13 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	int	i;
	int	num;
	int	cont;
	int	j;
	int	con;

	i = 2;
	num = atoi(argv[1]);
	con = 0;
	if (argc == 2)
	{
		if (num == 1)
			printf("1");
		else
		{
			while (i <= num)
			{
				j = 1;
				cont = 0;
				while (j <= i)
				{
					if (i % j == 0)
						cont++;
					j++;
				}
				if (cont == 2)
				{
					if (num % i == 0)
					{	
						while (num % i == 0)
						{
							con++;
		                                	if (con != 1)
		                                        	printf("*");
		                                	printf("%d", i);
							num = num / i;
						}	
					}
				}
				i++;
			}
		}	
	}
	printf("%s", "\n");
	return (0);
}
