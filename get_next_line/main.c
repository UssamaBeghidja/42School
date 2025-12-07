#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include "ft_get_next_line.h"

int main(void)
{
    int fd = open("test.txt", O_RDONLY);
    if (fd < 0)
    {
        perror("open");
        return 1;
    }

    char *line;
    int line_num = 1;

    while ((line = get_next_line(fd)) != NULL)
    {
        printf("Line %d: \"%s\"\n", line_num++, line);
        free(line);
    }

    close(fd);
    return 0;
}