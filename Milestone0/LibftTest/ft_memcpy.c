/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:26:05 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:50:03 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Copies memory from source to destination.
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
