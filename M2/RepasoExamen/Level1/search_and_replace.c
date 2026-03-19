/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   search_and_replace.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 22:29:15 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/05 22:47:03 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	main(int argc, char **argv)
{
	int	i;

	i = 0;
	if (argc == 4)
	{
		while (argv[1][i])
		{
			if ((ft_strlen(argv[2]) != 1) || ( ft_strlen(argv[3]) != 1))
				break ;
			else
			{
				if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
				{
					if ((argv[1][i] == argv[2][0]) && (argv[3][0] >= 'a' && argv[3][0]<= 'z'))
						write(1, &argv[3][0], 1);
					else
						write(1, &argv[1][i], 1);
				}
				else
					write(1, &argv[1][i], 1);
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
