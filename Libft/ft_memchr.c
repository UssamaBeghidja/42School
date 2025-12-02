char	*ft_memchr(void *str, int c, int size)
{
	int				i;
	unsigned char	*ptr;

	i = 0;
	*ptr = (unsigned char *)str;
	while (i < size)
	{
		if (ptr[i] == (unsigned char)c)
			return ((char *)&ptr[i]);
		i++;
	}
	return (0);
}
