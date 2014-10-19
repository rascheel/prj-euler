"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from sets import Set
from itertools import count

big_number = 600851475143


def main():
    factor_set = []
    for i in count(1):
        if( len(factor_set) > 0 and i == factor_set[-1]):
            break
        if(( big_number%i ) == 0):
            factor_set.append(i)
            factor_set.append(big_number / i)

    prime_factor_set = []
    for factor in factor_set:
        if is_prime(factor):
            prime_factor_set.append(factor)
    prime_factor_set.sort()
    print prime_factor_set[-1]

def is_prime(n):
    if(n == 1): return False

    for i in count(2):
        if i == n:
            break
        if( n%i == 0 ):
            return False
    return True


if __name__ == '__main__':
    main()
