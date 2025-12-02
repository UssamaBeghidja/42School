#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	count;

	if (!lst)
		return (NULL);
	count = 0;
	while (lst != NULL)
	{
		count++;
		lst = lst->next;
	}
	return (count);
}
