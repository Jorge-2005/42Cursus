/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 10:45:51 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 10:46:32 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	push_swap(t_list **list_a, t_list **list_b, int len)
{
	if (len == 2)
		sa(list_a);
	else if (len == 3)
		size3(list_a);
	else if (len == 4)
		short_size4(list_a, list_b, size4(list_a));
	else if (len == 5)
	{
		size5(list_a);
		pb(list_a, list_b);
		short_size4(list_a, list_b, size4(list_a));
		pa(list_a, list_b);
	}
	else
		radix_short(list_a, list_b, len);
}

int	*aux_main(char **arr, int len, t_list *list)
{
	int	i;
	int	*nums;

	i = 0;
	nums = malloc(len * sizeof(int));
	if (!nums)
		free_all_all(nums, arr, len, list);
	while (i < len)
	{
		nums[i] = ft_atol(arr[i]);
		i++;
	}
	ft_sort_int_tab(nums, len);
	if (duplicated(nums, len) == 0)
		free_all_all(nums, arr, len, list);
	return (nums);
}

void	add_list(int len, t_list **list_a, char **arr)
{
	int		i;
	long	num;

	i = 0;
	num = 0;
	while (i < len)
	{
		num = ft_atol(arr[i]);
		if (num > INT_MAX || num < INT_MIN)
		{
			free_all(arr, len);
			free_list(*list_a);
			ft_error();
		}
		ft_lstadd_back(list_a, ft_lstnew(num));
		i++;
	}
}

int	validate_input(char **argv)
{
	int	i;
	int	j;

	i = 1;
	while (argv[i])
	{
		j = 0;
		while (argv[i][j])
		{
			if (!(argv[i][j] >= '0' && argv[i][j] <= '9')
				&& argv[i][j] != ' ' && argv[i][j] != '+'
				&& argv[i][j] != '-' )
				return (1);
			if (argv[i][j] == '+' || argv[i][j] == '-')
			{
				if ((j != 0 && argv[i][j - 1] != ' ')
					||!(argv[i][j + 1] >= '0' && argv[i][j + 1] <= '9'))
					return (1);
			}
			j++;
		}
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	t_list	*list_a;
	t_list	*list_b;
	int		len;
	char	**arr;
	int		*nums;

	list_a = NULL;
	list_b = NULL;
	len = 0;
	if (argc < 2)
		return (0);
	if (validate_input(argv) == 1)
		ft_error();
	len = ft_len(argv);
	if (len == 0)
		return (0);
	arr = ft_getarr(argv, len, 1, 0);
	add_list(len, &list_a, arr);
	nums = aux_main(arr, len, list_a);
	set_index(nums, list_a, len);
	if (is_sorted(list_a))
		return (free_all(arr, len), free_list(list_a), free(nums), 0);
	free_all(arr, len);
	push_swap(&list_a, &list_b, len);
	return (free_list(list_a), free_list(list_b), free(nums), 0);
}
