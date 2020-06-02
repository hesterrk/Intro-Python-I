import sys


if len(sys.argv) == 2 and int(sys.argv[1]) % 2 == 0:
    print('Its a prime')


elif len(sys.argv) == 1:
    print('Please enter a prime')

elif int(sys.argv[1]) % 2 != 0:
    print('not a prime number')
