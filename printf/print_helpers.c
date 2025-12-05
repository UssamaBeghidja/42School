/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_helpers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 15:30:00 by u.b.             #+#    #+#             */
/*   Updated: 2025/12/05 15:30:00 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

int	ft_putchar_fd(int fd, char c)
{
	return (write(fd, &c, 1));
}

int	print_char(char c)
{
	return write(1, &c, 1);
}

int	print_default(char c)
{
	return (print_char(c));
}

int print_string(char *s)
{
    int count = 0;

    if (!s)
        s = "(null)";
    while (*s)
        count += print_char(*s++);
    return count;
}

int	ft_putnbr_base(unsigned long n, char *base)
{
	int				count;
	unsigned int	base_len;

	base_len = 0;
	count = 0;
	while (base[base_len])
		base_len++;
	if (n >= base_len)
		count += ft_putnbr_base(n / base_len, base);
	count += print_char(base[n % base_len]);
	return (count);
}

int	print_decimal(int n)
{
	unsigned int	nb;
	int				count;

	count = 0;
	if (n < 0)
	{
		count += print_char('-');
		nb = -n;
	}
	else
		nb = n;
	count += ft_putnbr_base(nb, "0123456789");
	return (count);
}

int	print_integer(int n)
{
	return (print_decimal(n));
}

int	print_unsigned_decimal(unsigned int n)
{
	return (ft_putnbr_base(n, "0123456789"));
}

int	print_hex_lower(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789abcdef"));
}

int	print_hex_upper(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789ABCDEF"));
}

int print_pointer(void *p)
{
    unsigned long addr;
    int count = 0;

    if (!p)
        return print_string("(nil)");
    count += print_string("0x");
    addr = (unsigned long)p;
    count += ft_putnbr_base(addr, "0123456789abcdef");
    return count;
}

int	print_percent(void)
{
	return (print_char('%'));
}
