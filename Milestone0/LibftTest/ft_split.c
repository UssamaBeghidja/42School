/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:27:00 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:56:12 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

// Counts how many words are in the string s separated by the delimiter c
static int	count_words(const char *s, char c)
{
	int	i;
	int	wc;

	i = 0;
	wc = 0;
	while (s[i])
	{
		if (s[i] != c && (i == 0 || s[i - 1] == c))
			wc++;
		i++;
	}
	return (wc);
}

//Splits a string into an array of strings using a delimiter.
char	**ft_split(char const *s, char c)
{
	char	**tab;
	int		i;
	int		j;
	int		start;

	if (!s)
		return (NULL);
	tab = ft_calloc(count_words(s, c) + 1, sizeof(char *));
	if (!tab)
		return (NULL);
	i = 0;
	j = 0;
	while (s[i])
	{
		while (s[i] == c)
			i++;
		if (!s[i])
			break ;
		start = i;
		while (s[i] && s[i] != c)
			i++;
		tab[j++] = ft_substr(s, start, i - start);
	}
	return (tab);
}
