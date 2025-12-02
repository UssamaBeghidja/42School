#include "libft.h"

void	ft_bzero(void *memory_location, int size)
{
	unsigned char	*ptr;

	*ptr = memory_location;
	while (size--)
	{
		*ptr = 0;
		ptr++;
	}
}
