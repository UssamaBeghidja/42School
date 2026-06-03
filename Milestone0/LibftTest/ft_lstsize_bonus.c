/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: giovanni <giovanni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 21:25:52 by ubeghidj          #+#    #+#             */
/*   Updated: 2025/12/03 22:02:31 by giovanni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

//Counts the number of nodes in a linked list.
int	ft_lstsize(t_list *lst)
{
	int	count;

	if (!lst)
		return (0);
	count = 0;
	while (lst != NULL)
	{
		count++;
		lst = lst->next;
	}
	return (count);
}
