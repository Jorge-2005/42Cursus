/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   expand_str.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/09 12:44:36 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/09 12:45:18 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	flag;

	i = 0;
	flag = 0;
	if (argc == 2)
	{
		while (argv[1][i] == ' ')
			i++;
		while (argv[1][i])
		{
			while (argv[1][i] == ' ')
			{
				i++;
				flag = 1;
			}
			if (flag == 1 && argv[1][i])
			{
				flag = 0;
				write(1, " ", 1);
				write(1, " ", 1);
				write(1, " ", 1);
			}
			if (argv[1][i] != ' ' && argv[1][i] != '\0')
			{
				write(1, &argv[1][i], 1);
				i++;
			}
		}
	}
	write(1, "\n", 1);
	return (0);
}
