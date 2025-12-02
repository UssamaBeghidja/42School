/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ubeghidj <ubeghidj@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:26:16 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/02 21:51:30 by ubeghidj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
