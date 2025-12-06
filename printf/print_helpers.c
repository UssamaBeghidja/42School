/* print_helpers.c */
#include "ft_printf.h"
#include <unistd.h>

/* low-level write wrapper */
int	ft_putchar_fd(int fd, char c)
{
	return (write(fd, &c, 1));
}

/* prints a single char and returns 1 */
int	print_char(char c)
{
	return (ft_putchar_fd(1, c));
}

/* fallback for unknown specifier */
int	print_default(char c)
{
	return (print_char(c));
}

/* prints string safely (handles NULL) */
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

/* recursive base printer for unsigned long and arbitrary base string */
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

/* decimal (signed) printing */
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

/* alias for %i -> same as %d */
int	print_integer(int n)
{
	return (print_decimal(n));
}

/* unsigned decimal */
int	print_unsigned_decimal(unsigned int n)
{
	return (ft_putnbr_base(n, "0123456789"));
}

/* hex lowercase */
int	print_hex_lower(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789abcdef"));
}

/* hex uppercase */
int	print_hex_upper(unsigned int x)
{
	return (ft_putnbr_base(x, "0123456789ABCDEF"));
}

/* pointer: prints (nil) for NULL, otherwise 0x... */
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

/* percent */
int	print_percent(void)
{
	return (print_char('%'));
}