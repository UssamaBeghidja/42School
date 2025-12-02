/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ubeghidj <ubeghidj@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:26:05 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/02 21:47:24 by ubeghidj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *destination, const void *src, size_t n)
{
	unsigned char	*ptr_src;
	unsigned char	*ptr_destination;
	size_t			i;

	ptr_src = (unsigned char *)src;
	ptr_destination = (unsigned char *)destination;
	i = 0;
	while (i < n)
	{
		*ptr_destination = *ptr_src;
		ptr_destination++;
		ptr_src++;
		i++;
	}
	return (destination);
}
