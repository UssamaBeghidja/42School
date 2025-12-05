# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -Werror

# Source files
SRC = ft_printf.c parse_helpers.c handle_helpers.c print_helpers.c main.c
OBJ = $(SRC:.c=.o)

# Header
HEADER = ft_printf.h

# Executable name
NAME = test_printf

all: $(NAME)

# Compile object files
%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

# Link objects to executable
$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

# Clean object files
clean:
	rm -f $(OBJ)

# Clean everything
fclean: clean
	rm -f $(NAME)

# Recompile everything
re: fclean all

.PHONY: all clean fclean re