#include <stddef.h>

void	ft_bzero(void *ptr, size_t n)
{
	unsigned char	*p;

	*p = ptr
		while (n--)
	{
		*p = 0;
		p++;
	}
}

void *ft_calloc(size_t count, size_t size)
{
	unsigned char *ptr;

	*ptr = malloc(count * size)
	if (!ptr)
		return (0);
	ft_bzero(ptr, count * size);
	return ptr;
}
