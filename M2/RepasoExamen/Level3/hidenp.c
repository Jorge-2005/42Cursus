/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hidenp.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/09 13:19:56 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/09 13:28:27 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	j;
	
	i = 0;
	j = 0;
	if (argc == 3)
	{
		while (argv[2][i])
		{
			if (argv[1][j] == argv[2][i])
				j++;
			i++;
		}
		if (argv[1][j] == '\0')
			write(1, "1", 1);
		else
			write(1, "0", 1);
	}
	write(1, "\n", 1);
	return (0);
}
