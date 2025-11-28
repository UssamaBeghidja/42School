char    *ft_strnstr(const char *haystack, const char *needle, int len)
{
    if (needle[0] == '\0')
        return (char *)haystack;
    if (len <= 0)
        return (0);

    int i = 0;
    while (i < len && haystack[i])
    {
        int j = 0;
        while (i + j < len && needle[j] && haystack[i + j] == needle[j])
            j++;
        if (needle[j] == '\0')
            return (char *)(haystack + i);
        i++;
    }
    return (0);
}