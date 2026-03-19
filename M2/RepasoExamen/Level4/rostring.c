/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rostring.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 17:14:56 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/12 19:20:55 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

int	count_word(char *str)
{
	int	i;
	int	cont;

	i = 0;
	cont = 0;
	while (str[i])
	{
		if (str[i] != ' ' && (str[i + 1] == ' ' || str[i + 1] == '\0'))
			cont++;
		i++;
	}
	return (cont);
}

int	main(int argc, char **argv)
{
	if (argc > 1)
	{
		int	i;
		int	contp;
		int	flag;
		int	j;

		i = 0;
		contp = 0;
		flag = 0;
		if (count_word(argv[1]) == 1)
		{
			while (argv[1][i] && (argv[1][i] == ' ' || argv[1][i] == '\t'))
				i++;
			while (argv[1][i])
			{
				if (argv[1][i] != ' ' && argv[1][i] != '\t')
					write(1, &argv[1][i], 1);
				i++;
			}
		}
		else
		{
			while (argv[1][i] && (argv[1][i] == ' ' || argv[1][i] == '\t'))
				i++;
			j = i;
			while ( argv[1][i] && (argv[1][i] != ' '))
			{
				i++;
				contp++;
			}
			i++;
			while (argv[1][i])
			{
				flag = 0;
				while (argv[1][i] == ' ' || argv[1][i] == '\t')
				{
					flag = 1;
					i++;
				}
				if (flag == 1)
				{
					write(1, " ", 1);
					flag = 0;
				}
				else if (flag != 1)
				{
					write(1, &argv[1][i], 1);
					i++;
				}
			}
			if (argv[1][i - 1] != ' ')
				write(1, " ", 1);
			while (j <= contp + 1)
			{
				write(1, &argv[1][j], 1);
				j++;
			}
		}
	}
	write(1, "\n", 1);
	return (0);
}
