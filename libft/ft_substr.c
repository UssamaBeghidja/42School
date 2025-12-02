/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 02:05:14 by aliabou-          #+#    #+#             */
/*   Updated: 2025/11/14 02:08:50 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_fs(char *dest, char const *src, unsigned int start, size_t sub_len)
{
	size_t	i;

	i = 0;
	while (i < sub_len)
	{
		dest[i] = src[start + i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*sub;
	size_t	s_len;
	size_t	sub_len;

	if (!s)
		return (NULL);
	s_len = ft_strlen(s);
	if (start >= s_len)
		sub_len = 0;
	else
	{
		sub_len = s_len - start;
		if (sub_len > len)
			sub_len = len;
	}
	sub = (char *)malloc(sizeof(char) * (sub_len + 1));
	if (!sub)
		return (NULL);
	return (ft_fs(sub, s, start, sub_len));
}
