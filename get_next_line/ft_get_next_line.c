/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_get_next_line.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: u.b. <u.b.@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/07 12:00:00 by student           #+#    #+#             */
/*   Updated: 2025/12/07 13:17:19 by u.b.             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include "ft_get_next_line.h"

char    *get_next_line(int fd)
{
    static char *leftover;
    char        buf[BUFFER_SIZE + 1];
    ssize_t     n;

    if (fd < 0 || BUFFER_SIZE <= 0)
        return (NULL);
    while (!leftover || !ft_strchr_gnl(leftover, '\n'))
    {
        n = read(fd, buf, BUFFER_SIZE);
        if (n <= 0)
            break ;
        buf[n] = '\0';
        if (!leftover)
            leftover = ft_strdup_gnl(buf);
        else
        {
            char *tmp = ft_strjoin_gnl(leftover, buf);
            free(leftover);
            leftover = tmp;
        }
    }
    return (extract_trim_line(&leftover));
}

char    *extract_trim_line(char **leftover)
{
    char    *new_leftover;
    int     len;
    int     i;
    char    *line;

    if (!*leftover || !**leftover)
        return (NULL);
    i = 0;
    while ((*leftover)[i] && (*leftover)[i] != '\n')
        i++;
    len = i;
    if ((*leftover)[i] == '\n')
        len++;
    line = malloc(sizeof(char) * (len + 1));
    if (!line)
        return (NULL);
    i = -1;
    while (++i < len)
        line[i] = (*leftover)[i];
    line[len] = '\0';
    new_leftover = ft_strdup_gnl((*leftover) + len);
    free(*leftover);
    *leftover = new_leftover;
    return (line);
}