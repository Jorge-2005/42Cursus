/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   alpha_mirror.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 18:42:01 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/06 19:14:26 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	cont;

	i = 0;
	cont = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (argv[1][i] >= 'a' && argv[1][i]<= 'm')
			{
				cont = argv[1][i] - 97;
				cont = 122 - cont;
				write(1, &cont, 1);	
			}
			else if (argv[1][i] >= 'n' && argv[1][i]<= 'z')
			{
				cont = 122 - argv[1][i];
				cont = 97 + cont;
				write(1, &cont, 1);
			}
			else if (argv[1][i] >= 'A' && argv[1][i]<= 'M')
                        {
                                cont = argv[1][i] - 65;
                                cont = 90 - cont;
                                write(1, &cont, 1);
                        }
                        else if (argv[1][i] >= 'n' && argv[1][i]<= 'z')
                        {
                                cont = 90 - argv[1][i];
                                cont = 65 + cont;
                                write(1, &cont, 1);
                        }
			else
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
