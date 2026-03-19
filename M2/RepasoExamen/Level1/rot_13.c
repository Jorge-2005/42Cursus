/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rot_13.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 20:27:18 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/05 21:40:28 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	letra;

	i = 0;
	if(argc == 2)
	{
		while (argv[1][i])
		{
			if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
			{
				if (argv[1][i] > 'm')
				{
					letra = 'z' - argv[1][i];
					letra = 13 - letra;
					letra = 96 + letra;
					write(1, &letra, 1);
				}
				else
				{
					letra = argv[1][i] + 13;
					write(1, &letra, 1);
				}
			}
			else if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
                        {
                                if (argv[1][i] > 'M')
                                {
                                        letra = 'Z' - argv[1][i];
                                        letra = 13 - letra;
                                        letra = 64 + letra;
                                        write(1, &letra, 1);
                                }
                                else
                                {
                                        letra = argv[1][i] + 13;
                                        write(1, &letra, 1);
                                }
                        }
			else
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write (1, "\n", 1);
	return (0);
}
