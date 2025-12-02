/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/25 13:58:33 by aabou-da          #+#    #+#             */
/*   Updated: 2025/11/14 04:51:44 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	is_separator(char a, char c)
{
	if (c == a)
		return (1);
	return (0);
}

int	size_word(char const *str, char c)
{
	int	length;

	length = 0;
	while (str[length] != '\0' && !is_separator(str[length], c))
		length++;
	return (length);
}

int	word_counter(char const *string, char c)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (string[i] != '\0')
	{
		while (string[i] != '\0' && is_separator(string[i], c))
			i++;
		if (string[i] == '\0')
			break ;
		count++;
		while (string[i] != '\0' && !is_separator(string[i], c))
			i++;
	}
	return (count);
}

int	faow(char const *string, char c, char **array, int total_words)
{
	int	i;
	int	word_index;
	int	word_len;

	i = 0;
	word_index = 0;
	word_len = 0;
	while (word_index < total_words)
	{
		while (string[i] != '\0' && is_separator(string[i], c))
			i++;
		word_len = size_word(&string[i], c);
		array[word_index] = malloc(sizeof(char) * (word_len + 1));
		ft_strncpy(array[word_index], &string[i], word_len);
		array[word_index][word_len] = '\0';
		i += word_len;
		word_index++;
	}
	array[word_index] = (NULL);
	return (0);
}

char	**ft_split(char const *s, char c)
{
	int		total_words;
	char	**array;

	total_words = word_counter(s, c);
	array = malloc(sizeof(char *) * (total_words + 1));
	if (!array)
		return (NULL);
	if (faow(s, c, array, total_words) < 0)
		return (NULL);
	return (array);
}
