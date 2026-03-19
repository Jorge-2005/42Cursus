/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repeat_alpha.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 18:58:08 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/05 19:08:50 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			j = 0;
			if (argv[1][i] >= 'a' && argv[1][i]<= 'z')
			{
				j = argv[1][i] - 97;
				while (j != -1)
				{
					write(1, &argv[1][i], 1);
					j--;
				}
			}
			else if (argv[1][i] >= 'A' && argv[1][i]<= 'Z')
                        {
                                j = argv[1][i] - 65;
                                while (j != -1)
                                {
                                        write(1, &argv[1][i], 1);
                                        j--;
                                }
                        }
			else
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
