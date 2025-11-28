char *ft_strdup(const char *str)
{
    size_t len = 0;
    while (str[len])
        len++;
    len++;
 `
    char *dest = malloc(len * sizeof(char));
    if (!dest)
        return (0);

    size_t i = 0;
    while (i < len)
    {
        dest[i] = str[i];
        i++;
    }
    return copy;
}