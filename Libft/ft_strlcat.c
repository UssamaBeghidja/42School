#include "libft.h"

unsigned int	ft_strlcat(char *dest, const char *src, unsigned int dest_size)
{
	unsigned int	dest_len;
	unsigned int	src_len;
	unsigned int	i;

	dest_len = ft_strlen(dest);
	src_len = ft_strlen(src);
	if (dest_size <= dest_len)
		return (dest_size + src_len);
	i = 0;
	while (src[i] && dest_len + i < dest_size - 1)
	{
		dest[dest_len + i] = src[i];
		i++;
	}
	dest[dest_len + i] = '\0';
	return (dest_len + src_len);
}
