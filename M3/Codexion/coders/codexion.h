/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/29 18:26:57 by jovillal          #+#    #+#             */
/*   Updated: 2026/08/29 18:27:06 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef CODEXION_H
# define CODEXION_H

# include <stdio.h>
# include <unistd.h>
# include <stdlib.h>
# include <pthread.h>

typedef struct s_dongle		t_dongle;
typedef struct s_coder		t_coder;
typedef struct s_sim		t_sim;

typedef struct s_sim
{
	int		number_of_coders;
	long	time_to_burnout;
	long	time_to_compile;
	long	time_to_debug;
	long	time_to_refactor;
	int		number_of_compiles_required;
	long	dongle_cooldown;
	int		scheduler;
	t_coder		*coders;
	t_dongle	*dongles;
}	t_sim;

typedef struct s_coder
{
	int		id;
	int		compile_count;
	long	last_cstart;
}	t_coder;

typedef struct s_dongle
{
	int	id;
	pthread_mutex_t	mutex;
}	t_dongle;

void	parse(int argc, char **argv, t_sim *sim);
int		main(int argc, char **argv);
int		ft_strcmp(const char *s1, const char *s2);
int		ft_atoi(const char *nptr);

#endif
