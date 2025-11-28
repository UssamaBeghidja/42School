void *memcpy(void *destination, const void *src, int size)
{
    unsigned char *ptr_src = src;
    unsigned char *ptr_destination = destination;
    while(size--)
    {
        *ptr_destination = *ptr_src;
        ptr_destination++;
        ptr_src++;
    }
    return (destination);
}