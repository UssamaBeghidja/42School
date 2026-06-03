/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 03:29:57 by aliabou-          #+#    #+#             */
/*   Updated: 2025/11/14 05:38:48 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_get_num_digits(long n)
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

static void	ft_fs(char *str, long n_abs, int is_negative, int total_len)
{
	str[total_len] = '\0';
	if (n_abs == 0)
	{
		str[0] = '0';
		return ;
	}
	total_len--;
	while (n_abs > 0)
	{
		str[total_len--] = (n_abs % 10) + '0';
		n_abs /= 10;
	}
	if (is_negative)
		str[total_len] = '-';
}

static char	*ft_handle_int_min(void)
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
	int		total_len;
	long	nb;
	int		is_negative;

	if (n == INT_MIN)
		return (ft_handle_int_min());
	is_negative = 0;
	if (n < 0)
		is_negative = 1;
	nb = n;
	if (is_negative)
		nb = -nb;
	total_len = ft_get_num_digits(nb);
	if (is_negative)
		total_len++;
	str = (char *)malloc(sizeof(char) * (total_len + 1));
	if (!str)
		return (NULL);
	ft_fs(str, nb, is_negative, total_len);
	return (str);
}
