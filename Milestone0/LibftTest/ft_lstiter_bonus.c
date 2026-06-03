/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:29 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:49:03 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Applies a function to each element of a linked list.
void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
		return ;
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}
