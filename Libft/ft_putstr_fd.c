void ft_putstr_fd(char *s, int fd)
{
    if (!s)
        return;
    int i = 0;
    while(s[i])
    {
        write(fd, &s[i], 1);
        i++;
    }
}