/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_helpers.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:40:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:24:44 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h>

/* ************************************************************************** */
/* handle_char_string:
 *   Handles %c, %s, and %% format specifiers.
 *   Returns the number of characters printed.
 *
 *   Notes:
 *     - Uses va_arg on *args to safely fetch the next argument.
 *     - Casts int to char for %c.
 *     - Checks for NULL pointer for %s internally in print_string.
 * ************************************************************************** */
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

/* ************************************************************************** */
/* handle_numbers:
 *   Handles numeric format specifiers: %d, %i, %u, %x, %X.
 *   Returns the number of characters printed.
 *
 *   Notes:
 *     - Uses va_arg on *args to fetch the correct type (int or unsigned int).
 *     - Calls the respective print function for each numeric type.
 * ************************************************************************** */
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

/* ************************************************************************** */
/* handle_pointer:
 *   Handles the %p format specifier (pointers).
 *   Returns the number of characters printed.
 *
 *   Notes:
 *     - Uses va_arg on *args to fetch the pointer (void *).
 *     - Calls print_pointer to print in "0x..." hexadecimal format.
 * ************************************************************************** */
int	handle_pointer(va_list *args, char spec)
{
	if (spec == 'p')
		return (print_pointer(va_arg(*args, void *)));
	return (-1);
}

/* ************************************************************************** */
/* handle_specifier:
 *   General dispatcher for a single format specifier.
 *   Calls the appropriate handler function based on the specifier.
 *   Returns the number of characters printed.
 *
 *   Notes:
 *     - Tries char/string first, then numbers, then pointer.
 *     - If none match, prints the specifier literally using print_default.
 * ************************************************************************** */
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
