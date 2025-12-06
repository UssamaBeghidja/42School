CC = gcc
CFLAGS = -Wall -Wextra -Werror

SRC = ft_printf.c parse_helpers.c handle_helpers.c print_helpers.c main.c
OBJ = $(SRC:.c=.o)
NAME = test_printf
HEADER = ft_printf.h

all: $(NAME)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re