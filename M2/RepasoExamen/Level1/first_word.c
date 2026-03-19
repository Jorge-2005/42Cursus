/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   first_word.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 20:47:23 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/04 20:47:45 by jovillal         ###   ########.fr       */
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
		while (argv[1][i] &&  cont != 1)
		{
			if (argv[1][i] != ' ' && (argv[1][i + 1] == ' ' || argv[1][i + 1] == '\0'))
				cont++;
			if (argv[1][i] != ' ')
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
