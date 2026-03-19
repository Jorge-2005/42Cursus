NAME			=	libftprintf.a

CC			=	cc
RM			=	rm -f
CFLAGS			=	-Wall -Wextra -Werror -I.

SRCS			= ft_printf.c util.c util2.c

OBJS			=	$(SRCS:.c=.o)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

all:			$(NAME)

$(NAME):		$(OBJS)
				ar rcs $(NAME) $(OBJS)

clean:
				$(RM) $(OBJS)

fclean:			clean
				$(RM) $(NAME)

re:			fclean $(NAME)

.PHONY:			all clean fclean re
