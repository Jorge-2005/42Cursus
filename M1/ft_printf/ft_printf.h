/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jovillal <jovillal@student.42malaga.c>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 17:11:16 by jovillal          #+#    #+#             */
/*   Updated: 2025/11/25 17:11:25 by jovillal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <unistd.h>
# include <stdio.h>
# include <stdlib.h>
# include <stdarg.h>

int				ft_printf(const char *type, ...);
int				ft_putchar(char c);
int				ft_putstr(char *s);
int				ft_putnbr(int n);
unsigned int	ft_putnbr_u(unsigned int n);
int				ft_hexmin(unsigned int n);
int				ft_hex(unsigned int n);
#endif
