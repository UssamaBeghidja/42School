/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_helpers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:55:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:24:01 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h>

/* ************************************************************************** */
/* handle_normal_char:
 *   Handles printing of a normal character (non-format specifier).
 *   Returns the number of characters printed (always 1).
 * ************************************************************************** */
int	handle_normal_char(char c)
{
	return (print_char(c));
}

/* ************************************************************************** */
/* handle_percent:
 *   Handles a '%' encountered in the format string.
 *   Parses the next character as a format specifier and calls handle_specifier.
 *   Returns the number of characters printed.
 *
 *   Notes:
 *     - *i is incremented to skip '%'.
 *     - Checks if the next character exists; if not, prints '%' literally.
 *     - Uses va_list *args to pass arguments safely to handle_specifier.
 * ************************************************************************** */
int	handle_percent(const char *format, int *i, va_list *args)
{
	int	count;

	(*i)++;
	if (!format[*i])
		return (print_percent());
	count = handle_specifier(args, format[*i]);
	(*i)++;
	return (count);
}

/* ************************************************************************** */
/* parse_format:
 *   Main parser for the format string.
 *   Loops through each character and delegates to handlers.
 *   Returns the total number of characters printed.
 *
 *   Notes:
 *     - If '%' is found, calls handle_percent.
 *     - Otherwise, prints the character literally using handle_normal_char.
 *     - va_list *args is passed to handlers for retrieving variadic arguments 
        safely.
 * ************************************************************************** */
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
