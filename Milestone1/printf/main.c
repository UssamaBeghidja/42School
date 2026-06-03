#include "ft_printf.h"
#include <stdio.h>  // for comparison

int main(void)
{
    int count;
    void *ptr = (void *)0x1234abcd;

    // ----- BASIC TESTS -----
    ft_printf("=== BASIC TESTS ===\n");
    ft_printf("Char: %c\n", 'A');
    ft_printf("String: %s\n", "Hello");
    ft_printf("Percent: %%\n");
    ft_printf("Decimal: %d\n", 42);
    ft_printf("Integer: %i\n", -42);
    ft_printf("Unsigned: %u\n", 3000000000u);

    // ----- HEX TESTS -----
    ft_printf("\n=== HEX TESTS ===\n");
    ft_printf("Hex lowercase: %x\n", 0xabcdef);
    ft_printf("Hex uppercase: %X\n", 0xABCDEF);
    ft_printf("Hex zero: %x\n", 0);

    // ----- POINTER TESTS -----
    ft_printf("\n=== POINTER TESTS ===\n");
    ft_printf("Pointer normal: %p\n", ptr);
    ft_printf("Pointer NULL: %p\n", NULL);

    // ----- MIX TESTS -----
    ft_printf("\n=== MIX TESTS ===\n");
    count = ft_printf("Mix1: %c %s %d %x %p\n", 'Z', "Hello", 1234, 0xabc, ptr);
    ft_printf("Printed %d characters\n", count);

    count = ft_printf("Mix2: %s %c %i %u %X %p\n",
            "World", '!', -42, 42u, 0xDEADBEEF, NULL);
    ft_printf("Printed %d characters\n", count);

    // ----- COMPARE WITH ORIGINAL printf -----
    ft_printf("\n=== COMPARE WITH REAL printf ===\n");
    int c1 = ft_printf("mine: [%d] [%s] [%p]\n", 99, "test", ptr);
    int c2 = printf   ("real: [%d] [%s] [%p]\n", 99, "test", ptr);

    ft_printf("my count = %d | real count = %d\n", c1, c2);

    return 0;
}