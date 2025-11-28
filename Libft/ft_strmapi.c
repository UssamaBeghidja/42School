char *ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
    if (!s)
        return NULL;
    int length = ft_strlen(s);
    char *new_string = malloc(length + 1);
    if (!new_string)
        return NULL;
    int i = 0;
    while (s[i])
    {
        new_string[i] = f(i, s[i]);
        i++;
    }
    new_string[i] = '\0';
    return (new_string);
}