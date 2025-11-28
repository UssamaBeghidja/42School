void *memmove(void *destination, const void *src, int size)
{ 
    if (destination > src && destination < src + size)
    {
        unsigned char *ptr_src = src + size - 1;
        unsigned char *ptr_destination = destination + size - 1;
        while(size--)
        {
          *ptr_destination = *ptr_src;
          ptr_destination--;
          ptr_src--;
        }
    }
    else {
        unsigned char *ptr_src = src;
        unsigned char *ptr_destination = destination;
        while(size--)
        {
            *ptr_destination = *ptr_src;
            ptr_destination++;
            ptr_src++;
        }
    }
    return (destination);
}