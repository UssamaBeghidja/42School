char *ft_itoa(int n)
{
    int sign = 1;
    char *result;
    if (n == 0)
    {
        result = malloc(2);
        if (!result) return NULL;
        result[0] = '0';
        result[1] = '\0';
        return (result);
    }
    if (n < 0)
    {
        sign = -1;
        n = n * (-1);
    }
    int length = 0;
    int temp = n;
    while (temp > 0)
    {
        temp = temp / 10;
        length++;
    }
    if (sign == -1)
        length++;
    result = malloc(length + 1);
    result[length] = '\0';
    int index = length -1;
    long num = n;
    if (num < 0)
        num = -num;
    int digit;
    while (num > 0)
    {
        digit = num % 10;
        result[index] = digit + '0';
        index--;
        num = num / 10;
    }
    if (sign == -1)
        result[0] = '-';
    return (result);
}