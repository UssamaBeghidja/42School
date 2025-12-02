/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ubeghidj <ubeghidj@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:24:29 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/02 21:36:32 by ubeghidj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
