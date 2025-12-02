/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ubeghidj <ubeghidj@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:07 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/02 23:55:10 by ubeghidj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_get_digits(long n)
{
	int	count;

	if (n == 0)
		return (1);
	count = 0;
	if (n < 0)
		n = -n;
	while (n > 0)
	{
		n /= 10;
		count++;
	}
	return (count);
}

static void	ft_fs(char *str, long n_abs, int is_negative, int tot_len)
{
	str[tot_len] = '\0';
	if (n_abs == 0)
	{
		str[0] = '0';
		return ;
	}
	tot_len--;
	while (n_abs > 0)
	{
		str[tot_len--] = (n_abs % 10) + '0';
		n_abs /= 10;
	}
	if (is_negative)
		str[tot_len] = '-';
}

static char	*ft_int_min(void)
{
	char	*str;

	str = (char *)malloc(sizeof(char) * 12);
	if (!str)
		return (NULL);
	ft_strlcpy(str, "-2147483648", 12);
	return (str);
}

char	*ft_itoa(int n)
{
	char	*str;
	int		tot_len;
	long	nb;
	int		is_negative;

	if (n == INT_MIN)
		return (ft_int_min());
	is_negative = 0;
	if (n < 0)
		is_negative = 1;
	nb = n;
	if (is_negative)
		nb = -nb;
	tot_len = ft_get_digits(nb);
	if (is_negative)
		tot_len++;
	str = (char *)malloc(sizeof(char) * (tot_len + 1));
	if (!str)
		return (NULL);
	ft_fs(str, nb, is_negative, tot_len);
	return (str);
}
