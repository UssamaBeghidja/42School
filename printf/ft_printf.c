#include "ft_printf.h"
#include <stdarg.h>

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	if (!format)
		return (0);
	va_start(args, format);
	count = parse_format(format, &args);
	va_end(args);
	return (count);
}
