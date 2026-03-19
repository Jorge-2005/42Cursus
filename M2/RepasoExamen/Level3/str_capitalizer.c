/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   str_capitalizer.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 17:47:31 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/11 18:32:35 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
				argv[1][i] = argv[1][i] + 32;
			i++;
		}
		i = 0;
		while (argv[1][i])
		{
			if  (i == 0 && argv[1][i] >= 'a' && argv[1][i] <= 'z')
				argv[1][i] = argv[1][i] - 32;
			else if ((argv[1][i] >= 'a' && argv[1][i] - 'z') && argv[1][i - 1] == ' ')
				argv[1][i] = argv[1][i] - 32;	
			write (1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
