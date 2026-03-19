/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   do_op.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 20:57:27 by jovillal          #+#    #+#             */
/*   Updated: 2026/03/06 21:11:58 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	if (argc == 4)
	{
		if (argv[2][0] == '+')
			printf("%d\n", atoi(argv[1]) + atoi(argv[3]));
		else if (argv[2][0] == '-')
                        printf("%d\n", atoi(argv[1]) - atoi(argv[3]));
		else if (argv[2][0] == '/')
                        printf("%d\n", atoi(argv[1]) / atoi(argv[3]));
		else if (argv[2][0] == '*')
                        printf("%d\n", atoi(argv[1]) * atoi(argv[3]));
		else if (argv[2][0] == '%')
                        printf("%i\n", atoi(argv[1]) % atoi(argv[3]));
	}
	return (0);
}
