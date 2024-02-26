#include <stdio.h>

/**
 * is_palindrome - checks if n is a palindrome
 * n: integer to check
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
    unsigned long reversed = 0;
    unsigned long original = n;

    // get the reverse number
    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }

    return (reversed == original) ? 1 : 0;
}