import sys

num = '1'

if len(sys.argv) == 2:
    num = int(sys.argv[1])

    if int(num) > 1:
        for i in range(2, num):
         if num % i == 0:
            print('Its NOT prime')


elif len(sys.argv) == 1:
    print('Please enter a prime')

elif num == 1:
    print('its a prime number')
