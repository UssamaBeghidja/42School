#include "ft_printf.h"

int	handle_normal_char(char c)
{
	return (print_char(c));
}

int	handle_percent(const char *format, int *i, va_list *args)
{
	int	count;

	(*i)++; /* skip '%' */
	if (!format[*i])
		return (print_percent());
	count = handle_specifier(args, format[*i]);
	(*i)++; /* skip specifier */
	return (count);
}

int	parse_format(const char *format, va_list *args)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%')
			count += handle_percent(format, &i, args);
		else
			count += handle_normal_char(format[i++]);
	}
	return (count);
}