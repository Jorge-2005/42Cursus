/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 17:48:36 by jovillal          #+#    #+#             */
/*   Updated: 2025/12/02 17:48:45 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "get_next_line.h"

char	*join_lines(int fd, char *arr)
{
	char	*buff;
	ssize_t	bytes;

	bytes = 1;
	buff = malloc(BUFFER_SIZE + 1);
	if (!buff)
		return (free(arr), NULL);
	if (!arr)
		arr = nul_join(arr);
	while (bytes > 0 && (ft_strchr(arr, '\n') == NULL))
	{
		bytes = read(fd, buff, BUFFER_SIZE);
		if (bytes < 0)
			return (free(arr), free(buff), NULL);
		buff[bytes] = '\0';
		arr = ft_strjoin(arr, buff);
		if (!arr)
			return (free(buff), NULL);
	}
	free(buff);
	return (arr);
}

char	*get_linen(char *arr)
{
	char	*buff;
	int		i;
	int		j;

	i = 0;
	j = 0;
	if (!arr)
		return (NULL);
	while (arr[i] != '\n' && arr[i])
		i++;
	if (arr[i] == '\n')
		i++;
	buff = malloc(i + 1);
	if (!buff)
		return (NULL);
	while (j < i)
	{
		buff[j] = arr[j];
		j++;
	}
	buff[j] = '\0';
	return (buff);
}

char	*get_new(char *arr)
{
	char	*buff;
	int		i;
	int		j;

	i = 0;
	j = 0;
	if (!arr)
		return (NULL);
	while (arr[i] != '\n' && arr[i])
		i++;
	if (arr[i] == '\n')
		i++;
	if (arr[i] == '\0')
	{
		free(arr);
		arr = NULL;
		return (NULL);
	}
	buff = malloc((ft_strlen(arr) - i) + 1);
	if (!buff)
		return (free(arr), NULL);
	while (arr[i])
		buff[j++] = arr[i++];
	buff[j] = '\0';
	return (free(arr), buff);
}

char	*get_next_line(int fd)
{
	static char	*arr = NULL;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	arr = join_lines(fd, arr);
	if (!arr)
		return (NULL);
	if (arr[0] == '\0')
	{
		free(arr);
		arr = NULL;
		return (NULL);
	}
	line = get_linen(arr);
	arr = get_new(arr);
	return (line);
}
/*
int	main(void)
{
	int	fd;

	fd = open("README.md", O_RDONLY);
	if (fd < 0)
		return (0);
	printf("%s", get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));istab01-j
	AAAAA
	close(fd);
	return (0);
}/*
int main(int argc, char **argv)
{
	(void)argc;
	int   fd;
    char *line;

    fd = open(argv[1], O_RDONLY);
    if (fd < 0)
        return (0);
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
}*/
