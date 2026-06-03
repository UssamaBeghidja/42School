/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:26:16 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:50:20 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Fills memory with a constant byte.
void	*ft_memset(void *memory_location, int value, size_t size)
{
	unsigned char	*ptr;
	size_t			i;

	ptr = (unsigned char *)memory_location;
	i = 0;
	while (i < size)
	{
		*ptr = (unsigned char)value;
		ptr++;
		i++;
	}
	return (memory_location);
}
