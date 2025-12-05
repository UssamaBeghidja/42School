/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_helpers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 15:20:00 by u.b.             #+#    #+#             */
/*   Updated: 2025/12/05 15:20:00 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h>

int	handle_normal_char(char c)
{
	return (print_char(c));
}

int	parse_format(const char *format, va_list args)
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
/*
int	handle_percent(const char *format, int *i, va_list args)
{
	if (format[*i + 1])
	{
		*i += 2;
		return (handle_specifier(args, format[*i - 1]));
	}
	*i += 1;
	return (print_percent_helper());
}*/
int handle_percent(const char *format, int *i, va_list args)
{
    int count = 0;

    (*i)++; // skip '%'
    if (!format[*i])
        return print_percent_helper(); // lone '%'

    count = handle_specifier(args, format[*i]); // read specifier
    (*i)++; // move past specifier
    return count;
}

int	handle_specifier(va_list args, char spec)
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
