/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:24:29 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:46:47 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Sets a memory area to zero.
void	ft_bzero(void *memory_location, size_t n)
{
	unsigned char	*ptr;
	size_t			i;

	ptr = (unsigned char *)memory_location;
	i = 0;
	while (i < n)
	{
		*ptr = 0;
		ptr++;
		i++;
	}
}
