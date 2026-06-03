/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:07 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:57:28 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

// Returns the number of characters needed to represent n as a string 
// (including '-' for negative numbers and '0')
int	len_int(int n)
{
	long	nb;
	int		len;

	nb = n;
	len = 0;
	if (nb <= 0)
		len++;
	if (nb < 0)
		nb = -nb;
	while (nb > 0)
	{
		len++;
		nb /= 10;
	}
	return (len);
}

//Converts an integer to a string.
char	*ft_itoa(int n)
{
	char	*str;
	long	nb;
	int		len;

	nb = n;
	len = len_int(n);
	str = malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	str[len] = '\0';
	if (nb < 0)
	{
		str[0] = '-';
		nb = -nb;
	}
	if (nb == 0)
		str[0] = '0';
	while (nb > 0)
	{
		str[len - 1] = (nb % 10) + '0';
		nb /= 10;
		len--;
	}
	return (str);
}
