int	ft_memcmp(const void *str1, const void *str2, int size)
{
	unsigned char	*ptr_str1;
	unsigned char	*ptr_str2;
	int				i;

	*ptr_str1 = str1;
	*ptr_str2 = str2;
	i = 0;
	while (i < size)
	{
		if (*ptr_str1 != *ptr_str2)
			return (*ptr_str1 - *ptr_str2);
		ptr_str1++;
		ptr_str2++;
		i++;
	}
	return (0);
}
