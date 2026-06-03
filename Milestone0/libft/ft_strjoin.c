/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliabou- <aliabou-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/25 13:53:05 by aabou-da          #+#    #+#             */
/*   Updated: 2025/11/14 04:44:05 by aliabou-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*joined_str;
	size_t	len1;
	size_t	len2;

	if (!s1 || !s2)
		return (NULL);
	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	joined_str = (char *)malloc(sizeof(char) * (len1 + len2 + 1));
	if (!joined_str)
		return (NULL);
	ft_strlcpy(joined_str, s1, len1 + 1);
	ft_strlcpy(joined_str + len1, s2, len2 + 1);
	return (joined_str);
}
