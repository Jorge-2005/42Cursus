/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/29 18:27:27 by jovillal          #+#    #+#             */
/*   Updated: 2026/08/29 18:27:30 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	print_err(char *str)
{
	fprintf(stderr, "Error: %s\n", str);
	exit(1);
}

static int	check(char *str)
{
	int	i;

	i = 0;
	if (!str || !*str)
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

static void	load_sim(char **argv, t_sim *sim)
{
	sim -> number_of_coders = atoi(argv[1]);
	sim -> time_to_burnout = (long)atoi(argv[2]);
	sim -> time_to_compile = (long)atoi(argv[3]);
	sim -> time_to_debug = (long)atoi(argv[4]);
	sim -> time_to_refactor = (long)atoi(argv[5]);
	sim -> number_of_compiles_required = atoi(argv[6]);
	sim -> dongle_cooldown = (long)atoi(argv[7]);
	sim -> scheduler = 1;
	if (ft_strcmp(argv[8], "fifo") == 0)
		sim -> scheduler = 0;
	if (sim -> number_of_coders < 1)
		print_err("Number of coders must be 1 or more");
	if (sim -> number_of_compiles_required < 1)
		print_err("Number of compiles required must be 1 or more");
}//preguntar si me falta aluna otra condicion

void	parse(int argc, char **argv, t_sim *sim)
{
	int	i;

	i = 1;
	if (argc != 9)
		print_err("You need 8 arguments");
	while (i < 8)
	{
		if (check(argv[i]) != 1)
			print_err("invalid argument");
		i++;
	}
	if (ft_strcmp(argv[8], "fifo") != 0 && ft_strcmp(argv[8], "edf") != 0)
		print_err("Last argument must be 'fifo' or 'edf'");
	load_sim(argv, sim);
}
