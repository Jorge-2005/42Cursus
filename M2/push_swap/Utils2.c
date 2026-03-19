/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Utils2.c                                            :+:      :+:    :+:  */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 11:00:54 by jovillal          #+#    #+#             */
/*   Updated: 2026/02/16 11:00:56 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_len(char **argv)
{
	int		i;
	int		j;
	char	**arr;
	int		len;

	i = 1;
	len = 0;
	while (argv[i])
	{
		j = 0;
		arr = ft_split(argv[i], ' ');
		if (!arr)
			ft_error();
		while (arr[j])
		{
			j++;
		}
		len += j;
		i++;
		free_all(arr, j);
	}
	return (len);
}

size_t	ft_strlen(const char *str)
{
	size_t	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	i = 0;
	if (size == 0)
		return (ft_strlen(src));
	while (src[i] && i < size - 1)
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (ft_strlen(src));
}

char	**ft_getarr(char **argv, int len, int i, int p)
{
	int		j;
	char	**arr;
	char	**arrs;

	arr = malloc((len + 1) * sizeof(char *));
	while (argv[i])
	{
		j = 0;
		arrs = ft_split(argv[i], ' ');
		if (!arrs)
			ft_error();
		while (arrs[j])
		{
			arr[p] = malloc(ft_strlen(arrs[j]) + 1);
			if (!arr[p])
				ft_error();
			ft_strlcpy(arr[p], arrs[j], ft_strlen(arrs[j]) + 1);
			j++;
			p++;
		}
		i++;
		free_all(arrs, j);
	}
	arr[p] = NULL;
	return (arr);
}

void	free_list(t_list *list)
{
	t_list	*tmp;

	while (list)
	{
		tmp = list->next;
		free(list);
		list = tmp;
	}
}
