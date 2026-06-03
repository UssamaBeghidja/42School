/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:27:56 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:52:49 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Removes specified characters from the beginning and end of a string.
char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;
	size_t	length;
	char	*trimmed_str;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	end = ft_strlen(s1);
	while (end > start && ft_strchr(set, s1[end - 1]))
		end--;
	length = end - start;
	trimmed_str = malloc(length + 1);
	if (!trimmed_str)
		return (NULL);
	ft_strlcpy(trimmed_str, s1 + start, length + 1);
	return (trimmed_str);
}
