/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_helpers_numbers.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 02:15:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:25:08 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

/* ************************************************************************** */
/* print_decimal:
 *   Prints a signed integer in decimal format (%d).
 *   Handles negative numbers by printing '-' and converting to unsigned.
 *   Returns the number of characters printed.
 * ************************************************************************** */
int	print_decimal(int n)
{
	unsigned int	nb;
	int				count;

	count = 0;
	if (n < 0)
	{
		count += print_char('-');
		nb = (unsigned int)(- (long)n);
	}
	else
		nb = (unsigned int)n;
	count += ft_putnbr_base(nb, "0123456789");
	return (count);
}

/* ************************************************************************** */
/* print_integer:
 *   Alias for %i specifier, behaves same as print_decimal.
 * ************************************************************************** */
int	print_integer(int n)
{
	return (print_decimal(n));
}

/* ************************************************************************** */
/* print_unsigned_decimal:
 *   Prints an unsigned integer in decimal (%u).
 * ************************************************************************** */
int	print_unsigned_decimal(unsigned int n)
{
	return (ft_putnbr_base(n, "0123456789"));
}

/* ************************************************************************** */
/* print_hex_lower:
 *   Prints an unsigned integer in lowercase hexadecimal (%x).
 * ************************************************************************** */
int	print_hex_lower(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789abcdef"));
}

/* ************************************************************************** */
/* print_hex_upper:
 *   Prints an unsigned integer in uppercase hexadecimal (%X).
 * ************************************************************************** */
int	print_hex_upper(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789ABCDEF"));
}
