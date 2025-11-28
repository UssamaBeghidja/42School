#include <stdlib.h>
#include "libft.h"

char **ft_split(char const *s, char c)
{
    int i = 0;
    int word_count = 0;
    while (s[i])
    {
       if (s[i] != c && (i == 0 || s[i - 1] == c))
        {
            word_count++;
        }
        i++;
    }
    char **result = malloc(sizeof(char *) * (word_count + 1));
    i = 0;
    int word_index = 0;
    while(s[i])
    {
        while (s[i] == c)
            i++;
        if (!s[i])
        break;

        int start = i;
        while (s[i] && s[i] != c)
            i++;
        int length = i - start;
        result[word_index] = malloc(length + 1);
        int j = 0;
        while (j < length)
        {
            result[word_index][j] = s[start + j];
            j++;
        }
        result[word_index][j] = '\0';
        word_index++;
    }
    result[word_index] = NULL; 
    return (result);
}