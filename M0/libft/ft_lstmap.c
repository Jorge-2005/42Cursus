/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 18:04:54 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/21 18:05:03 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*tmp;
	t_list	*list;
	void	*str;

	list = NULL;
	if (!lst)
		return (NULL);
	while (lst)
	{
		str = f(lst -> content);
		tmp = ft_lstnew(str);
		if (!tmp)
		{
			del(str);
			ft_lstclear(&list, del);
			return (NULL);
		}
		lst = lst -> next;
		ft_lstadd_back(&list, tmp);
	}
	return (list);
}
