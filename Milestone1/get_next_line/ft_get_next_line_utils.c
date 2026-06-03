/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_get_next_line_utils.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/07 12:00:00 by student           #+#    #+#             */
/*   Updated: 2025/12/07 13:08:00 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_get_next_line.h"

//Joins two strings into a new string.
char	*ft_strjoin_gnl(char const *s1, char const *s2)
{
	int		i;
	int		j;
	char	*new_string;

	if (!s1)
    	return ft_strdup_gnl(s2);
	if (!s2)
    	return NULL;
	new_string = malloc(ft_strlen_gnl(s1) + ft_strlen_gnl(s2) + 1);
	if (!new_string)
		return (NULL);
	i = 0;
	while (s1[i])
	{
		new_string[i] = s1[i];
		i++;
	}
	j = 0;
	while (s2[j])
	{
		new_string[i + j] = s2[j];
		j++;
	}
	new_string[i + j] = '\0';
	return (new_string);
}

char	*ft_strdup_gnl(const char *str)
{
	size_t	i;
	char	*dest;

	i = 0;
	if (!str)
		return (NULL);
	dest = malloc(sizeof(char) * (ft_strlen_gnl(str) + 1));
	if (!dest)
		return (NULL);
	while (str[i])
	{
		dest[i] = str[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

//Returns the length of a string.
size_t	ft_strlen_gnl(const char *str)
{
	size_t	i;

	i = 0;
	while (str[i])
	{
		i++;
	}
	return (i);
}

//Locates the first occurrence of a character in a string.
char	*ft_strchr_gnl(const char *str, int c)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == (char)c)
			return ((char *)&str[i]);
		i++;
	}
	if (str[i] == (char)c)
		return ((char *)&str[i]);
	return (NULL);
}
