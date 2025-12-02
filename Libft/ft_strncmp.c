int	ft_strncmp(char *dest, char *src, int size)
{
	int	i;

	i = 0;
	while (i < size && src[i] && dest[i])
	{
		if (dest[i] != src[i])
			return (dest[i] - src[i]);
		i++;
	}
	return (0);
}
