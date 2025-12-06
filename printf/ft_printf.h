#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int		ft_printf(const char *format, ...);

/* parsing helpers */
int		parse_format(const char *format, va_list *args);
int		handle_percent(const char *format, int *i, va_list *args);
int		handle_specifier(va_list *args, char spec);
int		handle_normal_char(char c);

/* specifier groups */
int		handle_char_string(va_list *args, char spec);
int		handle_numbers(va_list *args, char spec);
int		handle_pointer(va_list *args, char spec);

/* print helpers (signatures unchanged) */
int		ft_putchar_fd(int fd, char c);
int		print_char(char c);
int		print_string(char *s);
int		print_decimal(int n);
int		print_integer(int n);
int		print_unsigned_decimal(unsigned int n);
int		print_hex_lower(unsigned int x);
int		print_hex_upper(unsigned int x);
int		print_pointer(void *p);
int		print_percent(void);
int		print_default(char c);
int		ft_putnbr_base(unsigned long n, char *base);

#endif