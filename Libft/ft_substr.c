#include <stdlib.h>
#include "libft.h"

char    *ft_substr(char const *s, unsigned int start, size_t len)
{
    size_t  slen;
    char    *sub;

    if (!s)
        return (NULL);

    slen = 0;
    while (s[slen])
        slen++;

    if (start >= slen)
    {
        sub = malloc(1);
        if (!sub)
            return (NULL);
        sub[0] = '\0';
        return (sub);
    }

    if (len > slen - start)
        len = slen - start;

    sub = malloc(len + 1);
    if (!sub)
        return (NULL);

    ft_strlcpy(sub, s + start, len + 1);
    return (sub);
}