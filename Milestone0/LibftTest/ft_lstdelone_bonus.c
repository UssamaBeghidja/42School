/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:25 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 14:48:52 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Deletes a single node from a linked list.
void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (!lst || !del)
		return ;
	del(lst->content);
	free(lst);
}
