
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 15:10:00 by u.b.             #+#    #+#             */
/*   Updated: 2025/12/05 15:10:00 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

/* Low-level print functions */
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

/* Main ft_printf function */
int		ft_printf(const char *format, ...);

/* Internal helpers */
int		handle_normal_char(char c);
int		handle_numbers(va_list args, char spec);
int		handle_char_string(va_list args, char spec);
int		handle_pointer(va_list args, char spec);
int		handle_specifier(va_list args, char spec);
int		parse_format(const char *format, va_list args);
int		handle_percent(const char *format, int *i, va_list args);
int		print_percent_helper(void);
int		ft_putnbr_base(unsigned long n, char *base);

#endif