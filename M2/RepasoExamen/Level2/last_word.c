/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   last_word.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 23:41:16 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/08 00:04:08 by jovillal         ###   ########.fr       */
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
			i++;
		while (i > 0 && argv[1][i] == ' ')
			i--;
		while (i >= 0 && argv[1][i] != ' ')
			i--;
		i++;
		while (argv[1][i] >= 'a' && argv[1][i] <= 'z')//lo he deajdo asi, pero si se pone desde 33 hasta 126 ya tendrias todos los caracteres quitando el espacio que es 32
		{
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
