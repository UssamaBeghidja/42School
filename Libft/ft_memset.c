void *ft_memset(void *memory_location, int value, int size)
{
    unsigned char *ptr = memory_location;
    while (size--)
    {
        *ptr = value;
        ptr++;
    }
    return(memory_location);
}