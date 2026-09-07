/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/31 20:52:53 by jovillal          #+#    #+#             */
/*   Updated: 2026/08/31 20:52:57 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	in_coders(t_sim *sim)
{
	int	i;
	
	i = 0;
	sim -> coders = malloc(sim -> number_of_coders * sizeof(t_coder));
	if (!sim -> coders)
		return (1);
	while (i < sim -> number_of_coders)
	{
		sim -> coders[i].id = i + 1;
		sim -> coders[i].compile_count = 0;
		sim -> coders[i].last_cstart = 0;
		sim -> coders[i].sim_c = sim;
		if (i == (sim -> number_of_coders) - 1)
		{
			sim -> coders[i].rigth = &sim->dongles[0];
			sim -> coders[i].left = &sim->dongles[i];	
		}else
		{
			sim -> coders[i].left = &sim->dongles[i];
			sim -> coders[i].right = &sim->dongles[i + 1];
		}
		i++;
	}
	return (0);
}

int	in_dongles(t_sim *sim)
{
	int	i;
	
	i = 0;
	sim -> dongles = malloc(sim -> number_of_coders * sizeof(t_dongle));
	if (!sim->dongles)
		return (1);
	while (i < sim -> number_of_coders)
	{
		sim -> dongles[i].id = i + 1;
		if (pthread_mutex_init(&sim -> dongles[i].mutex, NULL) != 0)
			return (1)// con esto inicializo los mutex y doy error si falla alguno
		i++;
	}
	return (0);
}

/*
si no soy el último coder:
    left  = dongle[i]
    right = dongle[i + 1]

si soy el último:
    left  = dongle[i]
    right = dongle[0]
*/