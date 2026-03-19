/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Utils3.c                                            :+:      :+:    :+:  */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	is_sorted(t_list *list)
{
	t_list	*first;

	first = list;
	while (first -> next)
	{
		if (first -> value > first -> next -> value)
			return (0);
		first = first -> next;
	}
	return (1);
}

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	tmp = 0;
	while (i < size)
	{
		j = i;
		while (j < size)
		{
			if (tab[i] > tab[j])
			{
				tmp = tab[i];
				tab[i] = tab[j];
				tab[j] = tmp;
			}
			j++;
		}
		i++;
	}
}

int	duplicated(int *arr, int len)
{
	int	i;

	i = 0;
	while (i < len - 1)
	{
		if (arr[i] == arr[i + 1])
			return (0);
		i++;
	}
	return (1);
}

void	set_index(int *arr, t_list *list, int len)
{
	t_list	*first;
	int		value;
	int		i;

	first = list;
	while (first)
	{
		i = 0;
		value = first -> value;
		while (i < len)
		{
			if (arr[i] == value)
			{
				first -> index = i;
				break ;
			}
			i++;
		}
		first = first -> next;
	}
}

void	free_all_all(int *nums, char **arr, int len, t_list *list)
{
	free(nums);
	free_all(arr, len);
	free_list(list);
	ft_error();
}
