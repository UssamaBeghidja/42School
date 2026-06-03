/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 02:00:15 by aliabou-          #+#    #+#             */
/*   Updated: 2025/11/14 02:03:17 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	void	*ptr;
	size_t	total_size;

	if (count == 0 || size == 0)
	{
		return (malloc(0));
	}
	total_size = count * size;
	if (total_size / size != count)
	{
		return (NULL);
	}
	ptr = malloc(total_size);
	if (!ptr)
	{
		return (NULL);
	}
	ft_bzero(ptr, total_size);
	return (ptr);
}
