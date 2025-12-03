/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:26:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:49:54 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Compares two memory areas.
int	ft_memcmp(const void *str1, const void *str2, size_t size)
{
	const unsigned char	*ptr_str1;
	const unsigned char	*ptr_str2;
	size_t				i;

	ptr_str1 = (const unsigned char *)str1;
	ptr_str2 = (const unsigned char *)str2;
	i = 0;
	while (i < size)
	{
		if (ptr_str1[i] != ptr_str2[i])
			return (ptr_str1[i] - ptr_str2[i]);
		i++;
	}
	return (0);
}
