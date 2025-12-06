/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_helpers_symbols.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 02:15:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/06 09:20:48 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

/* ************************************************************************** */
/* ft_putnbr_base:
 *   Recursively prints an unsigned long number in the specified base.
 *   base: string containing characters representing digits, 
     e.g. "0123456789abcdef".
 *   Returns the total number of characters printed.
 * ************************************************************************** */
int	ft_putnbr_base(unsigned long n, char *base)
{
	int				count;
	unsigned int	base_len;

	count = 0;
	base_len = 0;
	while (base[base_len])
		base_len++;
	if (n >= base_len)
		count += ft_putnbr_base(n / base_len, base);
	count += print_char(base[n % base_len]);
	return (count);
}

/* ************************************************************************** */
/* print_pointer:
 *   Prints a pointer value (%p).
 *   Prints "(nil)" if the pointer is NULL.
 *   Otherwise prints in format "0x..." with lowercase hexadecimal digits.
 * ************************************************************************** */
int	print_pointer(void *p)
{
	unsigned long	addr;
	int				count;

	count = 0;
	if (!p)
		return (print_string("(nil)"));
	count += print_string("0x");
	addr = (unsigned long)p;
	count += ft_putnbr_base(addr, "0123456789abcdef");
	return (count);
}
