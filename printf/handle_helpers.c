#include "ft_printf.h"
#include <stdarg.h>

int	handle_char_string(va_list *args, char spec)
{
	if (spec == 'c')
		return (print_char((char)va_arg(*args, int)));
	if (spec == 's')
		return (print_string(va_arg(*args, char *)));
	if (spec == '%')
		return (print_percent());
	return (-1);
}

int	handle_numbers(va_list *args, char spec)
{
	if (spec == 'd')
		return (print_decimal(va_arg(*args, int)));
	else if (spec == 'i')
		return (print_integer(va_arg(*args, int)));
	else if (spec == 'u')
		return (print_unsigned_decimal(va_arg(*args, unsigned int)));
	else if (spec == 'x')
		return (print_hex_lower(va_arg(*args, unsigned int)));
	else if (spec == 'X')
		return (print_hex_upper(va_arg(*args, unsigned int)));
	return (-1);
}

int	handle_pointer(va_list *args, char spec)
{
	if (spec == 'p')
		return (print_pointer(va_arg(*args, void *)));
	return (-1);
}

int	handle_specifier(va_list *args, char spec)
{
	int	n;

	n = handle_char_string(args, spec);
	if (n != -1)
		return (n);
	n = handle_numbers(args, spec);
	if (n != -1)
		return (n);
	n = handle_pointer(args, spec);
	if (n != -1)
		return (n);
	return (print_default(spec));
}
