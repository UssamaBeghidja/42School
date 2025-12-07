#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

# include <stdlib.h>
# include <unistd.h>

char    *get_next_line(int fd);
char    *extract_trim_line(char **leftover);
char    *ft_strjoin_gnl(char const *s1, char const *s2);
char    *ft_strdup_gnl(const char *str);
size_t  ft_strlen_gnl(const char *str);
char    *ft_strchr_gnl(const char *str, int c);

#endif /* GET_NEXT_LINE_H */