unsigned int ft_strlcat(char *dest, const char *src, unsigned int dest_size)
{
    unsigned int dest_len = 0;
    unsigned int src_len = 0;
    unsigned int space_left = 0;
    unsigned int i = 0;
    
    while (dest[dest_len])
    {
        dest_len++;
    }
    while (src[src_len])
    {
        src_len++;
    }
    if (dest_size > dest_len)
        space_left = dest_size - dest_len - 1;
    else
        space_left = 0;

    if (dest_size > 0)
    {
        while(i < space_left && src[i])
        {
            dest[dest_len + i] = src[i];
            i++;
        }
        dest[dest_len + i] = '\0';
    }
    return(src_len + dest_len);
}