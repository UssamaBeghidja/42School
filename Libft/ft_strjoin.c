#include <stdlib.h>
#include "libft.h"

char *ft_strjoin(char const *s1, char const *s2)
{
    int i;
    int j;
    char *new_string;
    if (!s1 || !s2)
        return (NULL);
    new_string = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
    if (!new_string)
        return NULL;

    i = 0;
    while(s1[i])
    {
        new_string[i] = s1[i];
        i++;
    }
    j = 0;
    while(s2[j])
    {
        new_string[i + j] = s2[j];
        j++;
    }
    new_string[i + j] = '\0';
    return (new_string);
}