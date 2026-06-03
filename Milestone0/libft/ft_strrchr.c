/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 01:23:36 by aliabou-          #+#    #+#             */
/*   Updated: 2025/11/14 01:23:57 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char	*last_occurrence;

	last_occurrence = NULL;
	while (*s != '\0')
	{
		if (*s == (char)c)
			last_occurrence = (char *)s;
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return (last_occurrence);
}
