/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 17:11:16 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/25 17:11:25 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H
# include <unistd.h>
# include <stdio.h>
# include <stdlib.h>
# include <limits.h>

typedef struct s_list
{
	int				value;
	int				index;
	struct s_list	*next;
	struct s_list	*prev;
}	t_list;

void	swap(t_list **list);
void	sa(t_list **a);
void	sb(t_list **b);
void	ss(t_list **a, t_list **b);
t_list	*ft_lstnew(int value);
t_list	*ft_lstlast(t_list *lst);
void	ft_lstadd_back(t_list **list, t_list *new);
long	ft_atol(const char *nptr);
void	push(t_list **list, t_list **dst);
void	pa(t_list **a, t_list **b);
void	pb(t_list **a, t_list **b);
t_list	*ft_lstlast(t_list *list);
void	rotate(t_list **list);
void	ra(t_list **a);
void	rb(t_list **b);
void	rr(t_list **a, t_list **b);
void	reverse(t_list **list);
void	rra(t_list **a);
void	rrb(t_list **b);
void	rrr(t_list **a, t_list **b);
void	ft_error(void);
void	*free_all(char **arr, int j);
int		ft_len(char **argv);
char	**ft_getarr(char **argv, int len, int i, int p);
size_t	ft_strlen(const char *str);
char	**ft_split(char const *s, char c);
int		is_sorted(t_list *list);
void	ft_sort_int_tab(int *tab, int size);
int		duplicated(int *arr, int len);
void	set_index(int *arr, t_list *list, int len);
void	free_list(t_list *list);
void	free_all_all(int *nums, char **arr, int len, t_list *list);
int		num_bits(int len);
void	radix_short(t_list **a, t_list **b, int len);
void	size3(t_list **list_a);
int		size4(t_list **list_a);
void	short_size4(t_list **list_a, t_list **list_b, int real_pos);
void	size5(t_list **list_a);
#endif
