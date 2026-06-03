/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:17 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:48:36 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Adds a new node at the beginning of a linked list.
void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!new)
		return ;
	new->next = *lst;
	*lst = new;
}
