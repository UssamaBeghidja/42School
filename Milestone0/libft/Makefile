# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/24 02:07:21 by aliabou-          #+#    #+#              #
#    Updated: 2025/11/14 05:00:48 by aliabou-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

RM = rm -rdf

CFLAGS = -Wall -Wextra -Werror

SRC =	ft_bzero.c \
	ft_isascii.c \
	ft_isalnum.c \
	ft_isalpha.c \
	ft_isdigit.c \
	ft_isprint.c \
	ft_memcpy.c \
	ft_memmove.c \
	ft_memset.c \
	ft_strlen.c \
	ft_strlcpy.c \
	ft_strlcat.c \
	ft_toupper.c \
	ft_tolower.c \
	ft_strchr.c \
	ft_strrchr.c \
	ft_strncmp.c \
	ft_memchr.c \
	ft_memcmp.c \
	ft_strnstr.c \
	ft_atoi.c \
	ft_calloc.c \
	ft_strdup.c \
	ft_substr.c \
	ft_strjoin.c \
	ft_strtrim.c \
	ft_split.c \
	ft_itoa.c \
	ft_strmapi.c \
	ft_striteri.c \
	ft_putchar_fd.c \
	ft_putstr_fd.c \
	ft_putendl_fd.c \
	ft_putnbr_fd.c \
	ft_strncpy.c

AR = ar -rcs

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
		$(AR) $(NAME) $(OBJ)

clean:
	$(RM) $(OBJ)

fclean:
	$(RM) $(NAME)
	$(RM) $(OBJ)

re: fclean all

.PHONY: all clean fclean re