/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:27:16 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:51:37 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Applies a function to each character of a string with index.
void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	int	i;

	if (!s)
		return ;
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
	return ;
}
