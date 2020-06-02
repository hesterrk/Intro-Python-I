import sys

import sys


if len(sys.argv) == 2:
    num = int(sys.argv[1])
    if num <= 1:
        print('Not Valid!')

    else:
        for x in range(2, num):
            if num % x == 0:
                print('this is not a prime')
                break
            elif num % x != 0:
                print('this is a prime')
                break


else:
    print('Please enter a prime')


# Logic --> Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number
# using for loop


# int(sys.argv[1]) % 2 == 0:
#     print('Its a prime')
