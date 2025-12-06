/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 00:50:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:23:16 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

/* ************************************************************************** */
/*                               MAIN FUNCTION                                */
/* ************************************************************************** */

/* 
 * ft_printf:
 *   The main printf-like function. Accepts a format string and variable
 *   arguments.
 */
int		ft_printf(const char *format, ...);

/* ************************************************************************** */
/*                              PARSING HELPERS                               */
/* ************************************************************************** */

/* parse_format:
 *   Iterates through the format string and prints characters or calls
 *   specifier handlers.
 */
int		parse_format(const char *format, va_list *args);

/* handle_percent:
 *   Handles '%' character in the format string, calls the specifier handler.
 */
int		handle_percent(const char *format, int *i, va_list *args);

/* handle_specifier:
 *   Dispatches to the correct group handler based on the specifier.
 */
int		handle_specifier(va_list *args, char spec);

/* handle_normal_char:
 *   Prints normal characters (not part of a format specifier).
 */
int		handle_normal_char(char c);

/* ************************************************************************** */
/*                              SPECIFIER GROUPS                              */
/* ************************************************************************** */

/* handle_char_string:
 *   Handles %c, %s, and %% specifiers.
 */
int		handle_char_string(va_list *args, char spec);

/* handle_numbers:
 *   Handles numeric specifiers: %d, %i, %u, %x, %X.
 */
int		handle_numbers(va_list *args, char spec);

/* handle_pointer:
 *   Handles pointer specifier %p.
 */
int		handle_pointer(va_list *args, char spec);

/* ************************************************************************** */
/*                              PRINT HELPERS                                 */
/* ************************************************************************** */

/* Basic printing functions */
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