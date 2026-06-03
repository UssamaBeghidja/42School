/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_helpers_chars.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 02:15:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:19:32 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

/* ************************************************************************** */
/* ft_putchar_fd:
 *   Low-level write wrapper that writes a single character to a file descriptor.
 *   Returns the number of bytes written (always 1 for a char).
 * ************************************************************************** */
int	ft_putchar_fd(int fd, char c)
{
	return (write(fd, &c, 1));
}

/* ************************************************************************** */
/* print_char:
 *   Prints a single character to stdout.
 *   Returns 1 (number of characters printed).
 * ************************************************************************** */
int	print_char(char c)
{
	return (ft_putchar_fd(1, c));
}

/* ************************************************************************** */
/* print_default:
 *   Fallback printing function for unknown/unsupported format specifiers.
 *   Simply prints the character literally.
 * ************************************************************************** */
int	print_default(char c)
{
	return (print_char(c));
}

/* ************************************************************************** */
/* print_string:
 *   Prints a null-terminated string to stdout.
 *   Handles NULL pointers safely by printing "(null)".
 *   Returns the total number of characters printed.
 * ************************************************************************** */
int	print_string(char *s)
{
	int	count;

	count = 0;
	if (!s)
		s = "(null)";
	while (*s)
	{
		count += print_char(*s);
		s++;
	}
	return (count);
}

/* ************************************************************************** */
/* print_percent:
 *   Prints a literal '%' character (%% in format string).
 * ************************************************************************** */
int	print_percent(void)
{
	return (print_char('%'));
}
