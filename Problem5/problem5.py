"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""
import itertools

MIN_RANGE=1
MAX_RANGE=20

def main(min_range=MIN_RANGE, max_range=MAX_RANGE):

    for i in itertools.count(start=0, step=max_range):
        if(i != 0):
            is_evenly_divisible=True
            for j in range(min_range, max_range):
                if((i%j) != 0):
                    is_evenly_divisible=False
                    break
            if(is_evenly_divisible):
                print i
                break

if __name__ == '__main__':
    main()
