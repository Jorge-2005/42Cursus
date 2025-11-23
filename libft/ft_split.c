/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 16:10:35 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/15 18:05:18 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*free_all(char **arr, int j)
{
	int	i;

	i = 0;
	while (i < j)
	{
		free(arr[i]);
		arr[i] = NULL;
		i++;
	}
	free(arr);
	arr = NULL;
	return (arr);
}

void	put_arr(char **arr, const char *s, int i, char c)
{
	int	j;
	int	k;

	j = 0;
	k = 0;
	while (s[k])
	{
		if (s[k] != c)
			arr[i][j++] = s[k];
		else if (k > 0 && (s[k] == c && s[k - 1] != c))
		{
			arr[i++][j] = '\0';
			j = 0;
		}
		if (s[k] != c && s[k + 1] == '\0')
		{
			arr[i++][j] = '\0';
			j = 0;
		}
		k++;
	}
	arr[i] = NULL;
}

int	count_let(const char *s, char c, int k)
{
	int	i;
	int	cont;
	int	len;

	i = 0;
	cont = -1;
	len = 0;
	while (s[i])
	{
		if (s[i] != c && (i == 0 || s[i - 1] == c))
			cont++;
		if (k == cont && s[i] != c)
			len++;
		i++;
	}
	return (len);
}

int	count(const char *s, char c)
{
	int	i;
	int	cont;

	i = 0;
	cont = 0;
	while (s[i])
	{
		if (s[i] == c && i != 0 && s[i - 1] != c)
			cont++;
		if (s[i] != c && s[i + 1] == '\0')
			cont++;
		i++;
	}
	return (cont);
}

char	**ft_split(char const *s, char c)
{
	int		i;
	int		j;
	char	**arr;
	int		k;

	i = 0;
	j = 0;
	k = 0;
	if (!s)
		return (NULL);
	arr = malloc((count(s, c) + 1) * sizeof(char *));
	if (!arr)
		return (NULL);
	while (i < count(s, c))
	{
		arr[i] = malloc((count_let(s, c, i) + 1) * sizeof(char));
		if (!arr[i])
			return (free_all(arr, i));
		i++;
	}
	i = 0;
	put_arr(arr, s, i, c);
	return (arr);
}
/*
int	main(void)
{
	int	i;
	int	j;
	char	**arr;

	i = 0;
	arr = ft_split("      hola    que tal    ", ' ');
	while (arr[i])
	{
		j = 0;
		while (arr[i][j])
		{
			ft_putchar_fd(arr[i][j], 1);
			j++;
		}
		printf("%s", "\n");
		i++;
	}
	//printf("%d", count("hola mundo", ' '));
	return (0);
}
*/
