/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:20:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:13:26 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h>

/* ************************************************************************** */
/* ft_printf:
 *   Main printf-like function. Accepts a format string and variable arguments.
 *   Returns the total number of characters printed.
 *
 *   Steps:
 *     1. Check if the format string is NULL. If so, return 0.
 *     2. Initialize the variable argument list with va_start.
 *     3. Pass the format string and pointer to va_list to parse_format,
 *        which handles all specifiers and printing.
 *     4. Close the variable argument list with va_end.
 *     5. Return the total count of printed characters.
 * ************************************************************************** */
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
