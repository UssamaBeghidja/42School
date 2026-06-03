# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 12:00:00 by student           #+#    #+#              #
#    Updated: 2025/12/07 13:01:39 by u.b.             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Compiler
CC = gcc
CFLAGS = -Wall -Wextra -Werror

# Files
SRCS = main.c ft_get_next_line.c ft_get_next_line_utils.c
OBJS = $(SRCS:.c=.o)

# Executable name
NAME = test_gnl

# Default target
all: $(NAME)

# Compile executable
$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

# Compile .c -> .o
%.o: %.c get_next_line.h
	$(CC) $(CFLAGS) -c $< -o $@

# Clean object files
clean:
	rm -f $(OBJS)

# Clean object files + executable
fclean: clean
	rm -f $(NAME)

# Rebuild everything
re: fclean all

# Optional: allow custom BUFFER_SIZE at compile time
# make BUFFER_SIZE=100
ifdef BUFFER_SIZE
CFLAGS += -DBUFFER_SIZE=$(BUFFER_SIZE)
endif

.PHONY: all clean fclean re