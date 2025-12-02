char	*ft_strdup(const char *str)
{
	size_t	len;
	size_t	i;
	char	*dest;

	len = 0;
	while (str[len])
		len++;
	len++;
	*dest = malloc(len * sizeof(char));
	if (!dest)
		return (0);
	i = 0;
	while (i < len)
	{
		dest[i] = str[i];
		i++;
	}
	return (copy);
}
