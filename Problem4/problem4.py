"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
import itertools

DIGITS = 3

def main(digits=DIGITS):
    minimum = 10 ** (digits-1)
    maximum = (10 ** (digits)) - 1

    for (i,j) in itertools.combinations_with_replacement(range(maximum, minimum-1, -1), 2):
        if( is_palindrome( i*j ) ):
            print "%i x %i = %i" % (i, j, i*j)
            break

def is_palindrome(n):
    n_str = str(n)

    is_palindrome = True
    for i in range(0, len(n_str)/2):
        if( n_str[i] != n_str[ ((i+1)*-1)] ):
            is_palindrome = False
            break

    return is_palindrome

if __name__ == '__main__':
    main()
