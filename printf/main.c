#include "ft_printf.h"
#include <stdio.h>

int main(void)
{
    int count;
    char *str = "Hello World!";
    int num = 78613957;
    void *ptr = &num;

    // Character
    count = ft_printf("Char: %c\n", 'A');
    ft_printf("Printed %d characters\n\n", count);

    // String
    count = ft_printf("String: %s\n", str);
    ft_printf("Printed %d characters\n\n", count);

    // Decimal
    count = ft_printf("Decimal: %d\n", num);
    ft_printf("Printed %d characters\n\n", count);

    // Integer
    count = ft_printf("Integer: %i\n", -num);
    ft_printf("Printed %d characters\n\n", count);

    // Unsigned
    count = ft_printf("Unsigned: %u\n", 4000000000U);
    ft_printf("Printed %d characters\n\n", count);

    // Hex lowercase
    count = ft_printf("Hex lower: %x\n", num);
    ft_printf("Printed %d characters\n\n", count);

    // Hex uppercase
    count = ft_printf("Hex upper: %X\n", num);
    ft_printf("Printed %d characters\n\n", count);

    // Pointer
    count = ft_printf("Pointer: %p\n", ptr);
    ft_printf("Printed %d characters\n\n", count);

    // Percent
    count = ft_printf("Percent: %%\n");
    ft_printf("Printed %d characters\n\n", count);

    // Mix example
    count = ft_printf("Mix: char %c, string %s, int %d, hex %x, ptr %p\n",
                      'Z', "Test", 1234, 0xabc, ptr);
    ft_printf("Printed %d characters\n\n", count);

    return 0;
}