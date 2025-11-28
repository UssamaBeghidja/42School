char *ft_memchr(void *str, int c, int size)
{
    int i = 0;
    unsigned char *ptr = (unsigned char *)str;
    while (i < size)
    {
        if (ptr[i] == (unsigned char)c)
            return ((char *)&ptr[i]);
        i++;
    }
    return (0);
}